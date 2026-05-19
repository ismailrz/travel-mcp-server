import { NextRequest, NextResponse } from "next/server";
import { callTool } from "@/lib/mcp";

export async function POST(
  req: NextRequest,
  { params }: { params: Promise<{ tool: string }> }
) {
  try {
    const { tool } = await params;
    const args = await req.json();
    const result = await callTool(tool, args);
    return NextResponse.json({ data: result });
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
