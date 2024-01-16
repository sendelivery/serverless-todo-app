import TodoSection from "@/components/TodoSection";
import { todoApiEndpoint, todoApiKey } from "@/lib/consts";
import { type TodoEntry } from "@/lib/todoClient";

export default async function Page() {
  const response = await fetch(todoApiEndpoint, {
    headers: {
      "x-api-key": todoApiKey,
    },
    next: { revalidate: 7200 },
  });
  const entries: TodoEntry[] = await response.json();

  return <TodoSection entries={entries} />;
}
