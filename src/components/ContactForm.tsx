"use client";

import Script from "next/script";
import { useEffect, useState } from "react";

interface ContactFormProps {
  variant?: "default" | "gradient";
}

declare global {
  interface Window {
    medicalemojiTurnstileCallback?: (token: string) => void;
    medicalemojiTurnstileExpired?: () => void;
    turnstile?: {
      reset?: () => void;
    };
  }
}

export function ContactForm({ variant = "default" }: ContactFormProps) {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    subject: "",
    message: "",
  });
  const [turnstileToken, setTurnstileToken] = useState("");
  const [status, setStatus] = useState<"idle" | "sending" | "success" | "error">("idle");
  const [statusMessage, setStatusMessage] = useState("");
  const siteKey = process.env.NEXT_PUBLIC_TURNSTILE_SITE_KEY;

  useEffect(() => {
    window.medicalemojiTurnstileCallback = (token: string) => {
      setTurnstileToken(token);
      if (status === "error") {
        setStatus("idle");
        setStatusMessage("");
      }
    };
    window.medicalemojiTurnstileExpired = () => {
      setTurnstileToken("");
    };

    return () => {
      delete window.medicalemojiTurnstileCallback;
      delete window.medicalemojiTurnstileExpired;
    };
  }, [status]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!turnstileToken) {
      setStatus("error");
      setStatusMessage("Please complete the captcha before sending.");
      return;
    }

    setStatus("sending");
    setStatusMessage("");

    const response = await fetch("/api/contact", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        ...formData,
        turnstileToken,
      }),
    });

    if (!response.ok) {
      const data = (await response.json().catch(() => null)) as { error?: string } | null;
      setStatus("error");
      setStatusMessage(data?.error ?? "Message could not be sent. Please try again.");
      setTurnstileToken("");
      window.turnstile?.reset?.();
      return;
    }

    setStatus("success");
    setStatusMessage("Message sent. We will follow up by email.");
    setFormData({
      name: "",
      email: "",
      subject: "",
      message: "",
    });
    setTurnstileToken("");
    window.turnstile?.reset?.();
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const isGradient = variant === "gradient";
  const labelClass = `block text-sm font-medium ${isGradient ? "text-white" : "text-gray-700"}`;
  const inputClass = "mt-1 block w-full rounded-lg border border-gray-200 bg-white px-4 py-3 text-sm text-gray-900 shadow-sm transition-colors placeholder:text-gray-400 focus:border-[#3452ff] focus:outline-none focus:ring-2 focus:ring-[#3452ff]/20";
  const helperClass = `text-sm ${isGradient ? "text-white/85" : "text-gray-600"}`;
  const isSubmitDisabled = status === "sending" || !siteKey;

  return (
    <form onSubmit={handleSubmit} className="mx-auto max-w-lg space-y-4">
      {siteKey && <Script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer />}
      <div>
        <label
          htmlFor="name"
          className={labelClass}
        >
          Name
        </label>
        <input
          type="text"
          id="name"
          name="name"
          required
          value={formData.name}
          onChange={handleChange}
          className={inputClass}
          placeholder="Your name"
        />
      </div>
      <div>
        <label
          htmlFor="email"
          className={labelClass}
        >
          Email
        </label>
        <input
          type="email"
          id="email"
          name="email"
          required
          value={formData.email}
          onChange={handleChange}
          className={inputClass}
          placeholder="you@example.com"
        />
      </div>
      <div>
        <label
          htmlFor="subject"
          className={labelClass}
        >
          Subject
        </label>
        <input
          type="text"
          id="subject"
          name="subject"
          required
          value={formData.subject}
          onChange={handleChange}
          className={inputClass}
          placeholder="Subject"
        />
      </div>
      <div>
        <label
          htmlFor="message"
          className={labelClass}
        >
          Message
        </label>
        <textarea
          id="message"
          name="message"
          required
          rows={5}
          value={formData.message}
          onChange={handleChange}
          className={inputClass}
          placeholder="Your message..."
        />
      </div>
      {siteKey ? (
        <div
          className="cf-turnstile"
          data-sitekey={siteKey}
          data-callback="medicalemojiTurnstileCallback"
          data-expired-callback="medicalemojiTurnstileExpired"
          data-error-callback="medicalemojiTurnstileExpired"
        />
      ) : (
        <p className={helperClass}>Contact form captcha is not configured.</p>
      )}
      {statusMessage && (
        <p
          className={`text-sm ${
            status === "success" ? (isGradient ? "text-white" : "text-emerald-700") : isGradient ? "text-white" : "text-red-600"
          }`}
          role="status"
        >
          {statusMessage}
        </p>
      )}
      <button
        type="submit"
        disabled={isSubmitDisabled}
        className={`w-full min-h-[44px] rounded-lg px-6 py-3 text-sm font-semibold shadow-sm transition-all hover:shadow-md ${
          isGradient
            ? "bg-white text-gray-900 hover:bg-gray-50"
            : "bg-gradient-to-r from-[#3452ff] to-[#ff1053] text-white hover:opacity-90"
        } disabled:cursor-not-allowed disabled:opacity-60`}
      >
        {status === "sending" ? "Sending..." : "Send Message"}
      </button>
    </form>
  );
}
