"use client";

import { useState } from "react";

interface ContactFormProps {
  variant?: "default" | "gradient";
}

export function ContactForm({ variant = "default" }: ContactFormProps) {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    subject: "",
    message: "",
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const mailtoLink = `mailto:info@medicalemoji.org?subject=${encodeURIComponent(formData.subject)}&body=${encodeURIComponent(`Name: ${formData.name}\nEmail: ${formData.email}\n\n${formData.message}`)}`;
    window.location.href = mailtoLink;
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

  return (
    <form onSubmit={handleSubmit} className="mx-auto max-w-lg space-y-4">
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
      <button
        type="submit"
        className={`w-full min-h-[44px] rounded-lg px-6 py-3 text-sm font-semibold shadow-sm transition-all hover:shadow-md ${
          isGradient
            ? "bg-white text-gray-900 hover:bg-gray-50"
            : "bg-gradient-to-r from-[#3452ff] to-[#ff1053] text-white hover:opacity-90"
        }`}
      >
        Send Message
      </button>
    </form>
  );
}
