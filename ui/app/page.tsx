"use client";

import { useState } from "react";
import FlightsTab from "@/components/FlightsTab";
import HotelsTab from "@/components/HotelsTab";
import WeatherTab from "@/components/WeatherTab";
import PoiTab from "@/components/PoiTab";
import ItineraryTab from "@/components/ItineraryTab";
import BudgetTab from "@/components/BudgetTab";

const TABS = [
  { id: "flights", label: "✈️ Flights" },
  { id: "hotels", label: "🏨 Hotels" },
  { id: "weather", label: "🌤 Weather" },
  { id: "poi", label: "📍 Places" },
  { id: "itinerary", label: "🗺 Itinerary" },
  { id: "budget", label: "💰 Budget" },
] as const;

type Tab = (typeof TABS)[number]["id"];

export default function Home() {
  const [tab, setTab] = useState<Tab>("flights");

  return (
    <div>
      <div className="flex gap-1 border-b border-slate-200 mb-6 overflow-x-auto">
        {TABS.map((t) => (
          <button
            key={t.id}
            onClick={() => setTab(t.id)}
            className={`px-4 py-2 text-sm font-medium rounded-t whitespace-nowrap transition-colors ${
              tab === t.id
                ? "bg-white border border-b-white border-slate-200 -mb-px text-blue-600"
                : "text-slate-500 hover:text-slate-800"
            }`}
          >
            {t.label}
          </button>
        ))}
      </div>

      {tab === "flights" && <FlightsTab />}
      {tab === "hotels" && <HotelsTab />}
      {tab === "weather" && <WeatherTab />}
      {tab === "poi" && <PoiTab />}
      {tab === "itinerary" && <ItineraryTab />}
      {tab === "budget" && <BudgetTab />}
    </div>
  );
}
