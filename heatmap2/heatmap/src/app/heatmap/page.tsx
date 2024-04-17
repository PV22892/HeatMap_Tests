"use client";
import dynamic from "next/dynamic";

const DynamicMap = dynamic(() => import("@/components/map"), { ssr: false });

export default function PostsPage() {
  return (
    <main className="text-center pt-16 px-5">
      <h1 className="text-5xl font-semibold mb-7">All posts</h1>
      <DynamicMap />
    </main>
  );
}
