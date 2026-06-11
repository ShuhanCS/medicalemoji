"use client";

import Link from "next/link";
import { useSyncExternalStore } from "react";
import { ArrowRight, X } from "lucide-react";

const DISMISS_KEY = "acep-announcement-dismissed";

const listeners = new Set<() => void>();

function subscribe(onChange: () => void) {
  listeners.add(onChange);
  window.addEventListener("storage", onChange);
  return () => {
    listeners.delete(onChange);
    window.removeEventListener("storage", onChange);
  };
}

function isDismissed() {
  return window.localStorage.getItem(DISMISS_KEY) === "true";
}

function dismiss() {
  window.localStorage.setItem(DISMISS_KEY, "true");
  listeners.forEach((fn) => fn());
}

export function AnnouncementBanner() {
  // Server renders the banner (false); the client reads localStorage on mount.
  const dismissed = useSyncExternalStore(subscribe, isDismissed, () => false);

  if (dismissed) {
    return null;
  }

  return (
    <div className="relative bg-gradient-to-r from-[#3452ff] to-[#ff1053] text-white">
      <div className="mx-auto flex max-w-7xl items-center justify-center gap-3 px-10 py-2.5 sm:px-12">
        <Link
          href="/endorsements"
          className="group flex flex-wrap items-center justify-center gap-x-2 gap-y-0.5 text-center text-sm font-medium"
        >
          <span aria-hidden="true">🚨</span>
          <span>
            <strong className="font-semibold">New:</strong> The American College of Emergency
            Physicians supports the Medical Emoji Project
          </span>
          <span className="inline-flex items-center gap-1 font-semibold underline-offset-2 group-hover:underline">
            Read more
            <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5" aria-hidden="true" />
          </span>
        </Link>
      </div>
      <button
        type="button"
        onClick={dismiss}
        aria-label="Dismiss announcement"
        className="absolute right-1 top-1/2 flex h-11 w-11 -translate-y-1/2 items-center justify-center text-white/80 transition-colors hover:text-white"
      >
        <X className="h-4 w-4" aria-hidden="true" />
      </button>
    </div>
  );
}
