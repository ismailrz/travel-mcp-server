from __future__ import annotations

from pydantic import BaseModel

CATEGORIES = ["flights", "hotels", "food", "activities", "transport", "shopping", "misc"]


class Expense(BaseModel):
    category: str
    amount: float
    description: str


class BudgetRecord(BaseModel):
    trip_id: str
    total_budget: float
    currency: str
    expenses: list[Expense] = []


_budgets: dict[str, BudgetRecord] = {}


def create(trip_id: str, total_budget: float, currency: str = "USD") -> dict:
    record = BudgetRecord(trip_id=trip_id, total_budget=total_budget, currency=currency)
    _budgets[trip_id] = record
    return {
        "trip_id": trip_id,
        "total_budget": total_budget,
        "currency": currency,
        "categories": {cat: 0.0 for cat in CATEGORIES},
        "message": f"Budget of {currency} {total_budget:.2f} created for trip '{trip_id}'.",
    }


def add_expense(trip_id: str, category: str, amount: float, description: str) -> dict:
    if trip_id not in _budgets:
        return {"error": f"No budget found for trip_id '{trip_id}'. Use create_trip_budget first."}
    cat = category if category in CATEGORIES else "misc"
    _budgets[trip_id].expenses.append(Expense(category=cat, amount=amount, description=description))
    return get_summary(trip_id)


def get_summary(trip_id: str) -> dict:
    if trip_id not in _budgets:
        return {"error": f"No budget found for trip_id '{trip_id}'."}

    record = _budgets[trip_id]
    category_totals: dict[str, float] = {cat: 0.0 for cat in CATEGORIES}
    for expense in record.expenses:
        cat = expense.category if expense.category in CATEGORIES else "misc"
        category_totals[cat] += expense.amount

    total_spent = sum(category_totals.values())
    remaining = record.total_budget - total_spent

    breakdown = {}
    for cat, spent in category_totals.items():
        pct = (spent / record.total_budget * 100) if record.total_budget > 0 else 0.0
        breakdown[cat] = {
            "spent": round(spent, 2),
            "percentage_of_budget": round(pct, 1),
        }

    return {
        "trip_id": trip_id,
        "currency": record.currency,
        "total_budget": record.total_budget,
        "total_spent": round(total_spent, 2),
        "remaining_balance": round(remaining, 2),
        "budget_used_pct": round(total_spent / record.total_budget * 100, 1) if record.total_budget > 0 else 0.0,
        "category_breakdown": breakdown,
        "expenses": [
            {"category": e.category, "amount": e.amount, "description": e.description}
            for e in record.expenses
        ],
    }
