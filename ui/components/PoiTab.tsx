"use client";

import { useState } from "react";
import { Card, Field, Input, Select, RunButton, ResultBox } from "./ui";

const CATEGORIES = ["restaurants", "attractions", "activities", "nightlife", "shopping", "transport"];

export default function PoiTab() {
  const [destination, setDestination] = useState("Tokyo");
  const [category, setCategory] = useState("attractions");
  const [limit, setLimit] = useState("5");
  const [result, setResult] = useState<unknown>();
  const [error, setError] = useState<string>();
  const [loading, setLoading] = useState(false);

  async function submit() {
    setLoading(true);
    setError(undefined);
    try {
      const res = await fetch("/api/tools/search_poi", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ destination, category, limit: Number(limit) }),
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
      <h2 className="text-base font-semibold mb-4">Points of Interest</h2>
      <div className="grid grid-cols-3 gap-4">
        <Field label="Destination">
          <Input value={destination} onChange={(e) => setDestination(e.target.value)} />
        </Field>
        <Field label="Category">
          <Select value={category} onChange={(e) => setCategory(e.target.value)}>
            {CATEGORIES.map((c) => (
              <option key={c} value={c}>{c}</option>
            ))}
          </Select>
        </Field>
        <Field label="Limit">
          <Input type="number" min={1} max={20} value={limit} onChange={(e) => setLimit(e.target.value)} />
        </Field>
      </div>
      <RunButton loading={loading} onClick={submit} />
      <ResultBox data={result} error={error} />
    </Card>
  );
}
