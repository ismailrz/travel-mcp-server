const MCP_BASE = process.env.MCP_SERVER_URL ?? "http://localhost:8000";

export async function callTool<T = unknown>(
  tool: string,
  args: Record<string, unknown>
): Promise<T> {
  const res = await fetch(`${MCP_BASE}/api/tools/${tool}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(args),
    cache: "no-store",
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`${tool} failed (${res.status}): ${text}`);
  }
  return res.json();
}
