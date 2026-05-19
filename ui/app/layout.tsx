import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Travel MCP Planner",
  description: "AI-powered travel planning tools",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-slate-50 text-slate-900 antialiased">
        <header className="bg-white border-b border-slate-200 px-6 py-4 flex items-center gap-3">
          <span className="text-2xl">✈️</span>
          <h1 className="text-xl font-semibold tracking-tight">Travel Planner</h1>
          <span className="ml-auto text-xs text-slate-400 font-mono">MCP Server</span>
        </header>
        <main className="max-w-5xl mx-auto px-6 py-8">{children}</main>
      </body>
    </html>
  );
}
