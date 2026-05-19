"use client";

import { useState } from "react";
import { Card, Field, Input, RunButton, ResultBox } from "./ui";

export default function WeatherTab() {
  const [destination, setDestination] = useState("Tokyo");
  const [from, setFrom] = useState("2026-07-01");
  const [to, setTo] = useState("2026-07-07");
  const [result, setResult] = useState<unknown>();
  const [error, setError] = useState<string>();
  const [loading, setLoading] = useState(false);

  async function submit() {
    setLoading(true);
    setError(undefined);
    try {
      const res = await fetch("/api/tools/get_weather", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ destination, date_from: from, date_to: to }),
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
      <h2 className="text-base font-semibold mb-4">Weather Forecast</h2>
      <div className="grid grid-cols-3 gap-4">
        <Field label="Destination">
          <Input value={destination} onChange={(e) => setDestination(e.target.value)} />
        </Field>
        <Field label="From">
          <Input type="date" value={from} onChange={(e) => setFrom(e.target.value)} />
        </Field>
        <Field label="To">
          <Input type="date" value={to} onChange={(e) => setTo(e.target.value)} />
        </Field>
      </div>
      <RunButton loading={loading} onClick={submit} />
      <ResultBox data={result} error={error} />
    </Card>
  );
}
