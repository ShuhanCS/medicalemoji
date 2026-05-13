import { Check, ExternalLink, FileText } from "lucide-react";
import type { Supporter } from "@/data/emoji";

interface SupportListProps {
  supporters: Supporter[];
}

export function SupportList({ supporters }: SupportListProps) {
  if (supporters.length === 0) {
    return null;
  }

  return (
    <section className="bg-white py-16">
      <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
        <h2 className="text-center text-2xl font-bold text-gray-900 sm:text-3xl">
          Supporting Organizations
        </h2>
        <p className="mx-auto mt-3 max-w-2xl text-center text-gray-600">
          The following organizations have expressed their support for this emoji proposal.
        </p>
        <div className="mt-8 grid gap-3 sm:grid-cols-2">
          {supporters.map((supporter) => {
            const content = (
              <>
                <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-gradient-to-r from-[#3452ff] to-[#ff1053]">
                  <Check className="h-4 w-4 text-white" aria-hidden="true" />
                </div>
                <span className="min-w-0 flex-1 text-sm font-medium text-gray-800">
                  {supporter.name}
                </span>
                {supporter.href ? (
                  <span className="flex shrink-0 items-center gap-1 text-xs font-semibold text-[#3452ff]">
                    <FileText className="h-3.5 w-3.5" aria-hidden="true" />
                    {supporter.linkLabel ?? "View letter"}
                    {supporter.href.startsWith("http") ? (
                      <ExternalLink className="h-3.5 w-3.5" aria-hidden="true" />
                    ) : null}
                  </span>
                ) : null}
              </>
            );

            if (supporter.href) {
              return (
                <a
                  key={supporter.name}
                  href={supporter.href}
                  target="_blank"
                  rel="noreferrer"
                  className="flex items-center gap-3 rounded-lg border border-gray-100 bg-gray-50 px-5 py-4 shadow-sm transition-colors hover:border-[#3452ff]/30 hover:bg-white"
                >
                  {content}
                </a>
              );
            }

            return (
              <div
                key={supporter.name}
                className="flex items-center gap-3 rounded-lg border border-gray-100 bg-gray-50 px-5 py-4 shadow-sm"
              >
                {content}
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
