"use client";

import { useState } from "react";
import { Card, Field, Input, Select, RunButton, ResultBox } from "./ui";

const EXPENSE_CATEGORIES = ["flights", "hotels", "food", "activities", "transport", "shopping", "misc"];

export default function BudgetTab() {
  const [tripId, setTripId] = useState("tokyo-jul-2026");

  // create budget
  const [totalBudget, setTotalBudget] = useState("5000");
  const [currency, setCurrency] = useState("USD");

  // add expense
  const [expCat, setExpCat] = useState("flights");
  const [expAmount, setExpAmount] = useState("");
  const [expDesc, setExpDesc] = useState("");

  const [result, setResult] = useState<unknown>();
  const [error, setError] = useState<string>();
  const [loading, setLoading] = useState(false);

  async function post(tool: string, args: Record<string, unknown>) {
    setLoading(true);
    setError(undefined);
    try {
      const res = await fetch(`/api/tools/${tool}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(args),
      });
      const data = await res.json();
      if (data.error) setError(data.error);
      else setResult(data.data);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-4">
      <Card>
        <h2 className="text-base font-semibold mb-4">Budget Tracker</h2>
        <Field label="Trip ID">
          <Input value={tripId} onChange={(e) => setTripId(e.target.value)} placeholder="my-trip-2026" />
        </Field>
      </Card>

      <Card>
        <h3 className="text-sm font-semibold mb-3 text-slate-600">Create Budget</h3>
        <div className="grid grid-cols-2 gap-4">
          <Field label="Total budget">
            <Input type="number" value={totalBudget} onChange={(e) => setTotalBudget(e.target.value)} />
          </Field>
          <Field label="Currency">
            <Input value={currency} onChange={(e) => setCurrency(e.target.value)} placeholder="USD" />
          </Field>
        </div>
        <RunButton
          loading={loading}
          onClick={() => post("create_trip_budget", { trip_id: tripId, total_budget: Number(totalBudget), currency })}
        />
      </Card>

      <Card>
        <h3 className="text-sm font-semibold mb-3 text-slate-600">Add Expense</h3>
        <div className="grid grid-cols-3 gap-4">
          <Field label="Category">
            <Select value={expCat} onChange={(e) => setExpCat(e.target.value)}>
              {EXPENSE_CATEGORIES.map((c) => <option key={c} value={c}>{c}</option>)}
            </Select>
          </Field>
          <Field label="Amount">
            <Input type="number" value={expAmount} onChange={(e) => setExpAmount(e.target.value)} placeholder="USD" />
          </Field>
          <Field label="Description">
            <Input value={expDesc} onChange={(e) => setExpDesc(e.target.value)} placeholder="ANA flight JFK→NRT" />
          </Field>
        </div>
        <RunButton
          loading={loading}
          onClick={() =>
            post("add_expense", {
              trip_id: tripId,
              category: expCat,
              amount: Number(expAmount),
              description: expDesc,
            })
          }
        />
      </Card>

      <Card>
        <h3 className="text-sm font-semibold mb-3 text-slate-600">Budget Summary</h3>
        <RunButton loading={loading} onClick={() => post("get_budget_summary", { trip_id: tripId })} />
      </Card>

      <ResultBox data={result} error={error} />
    </div>
  );
}
