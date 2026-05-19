"use client";

import { useState } from "react";
import { Card, Field, Input, RunButton, ResultBox } from "./ui";

export default function HotelsTab() {
  const [destination, setDestination] = useState("Tokyo");
  const [checkIn, setCheckIn] = useState("2026-07-01");
  const [checkOut, setCheckOut] = useState("2026-07-07");
  const [guests, setGuests] = useState("2");
  const [maxPrice, setMaxPrice] = useState("");
  const [result, setResult] = useState<unknown>();
  const [error, setError] = useState<string>();
  const [loading, setLoading] = useState(false);

  async function submit() {
    setLoading(true);
    setError(undefined);
    try {
      const res = await fetch("/api/tools/search_hotels", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          destination,
          check_in: checkIn,
          check_out: checkOut,
          guests: Number(guests),
          ...(maxPrice && { max_price: Number(maxPrice) }),
        }),
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
    <Card>
      <h2 className="text-base font-semibold mb-4">Search Hotels</h2>
      <div className="grid grid-cols-2 gap-4">
        <Field label="Destination">
          <Input value={destination} onChange={(e) => setDestination(e.target.value)} />
        </Field>
        <Field label="Max price / night (optional)">
          <Input type="number" value={maxPrice} onChange={(e) => setMaxPrice(e.target.value)} placeholder="USD" />
        </Field>
        <Field label="Check-in">
          <Input type="date" value={checkIn} onChange={(e) => setCheckIn(e.target.value)} />
        </Field>
        <Field label="Check-out">
          <Input type="date" value={checkOut} onChange={(e) => setCheckOut(e.target.value)} />
        </Field>
        <Field label="Guests">
          <Input type="number" min={1} value={guests} onChange={(e) => setGuests(e.target.value)} />
        </Field>
      </div>
      <RunButton loading={loading} onClick={submit} />
      <ResultBox data={result} error={error} />
    </Card>
  );
}
