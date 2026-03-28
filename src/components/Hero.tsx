import Link from "next/link";
import Image from "next/image";

const floatingEmoji = [
  { src: "/images/emoji/kidneysnew2.png", alt: "Kidney", size: 90, top: "8%", left: "5%", delay: "0s", duration: "6s" },
  { src: "/images/emoji/5-liver.png", alt: "Liver", size: 75, top: "15%", right: "8%", delay: "1s", duration: "7s" },
  { src: "/images/emoji/3-stomach.png", alt: "Stomach", size: 65, top: "65%", left: "3%", delay: "0.5s", duration: "8s" },
  { src: "/images/emoji/13-ecg-1.png", alt: "EKG", size: 80, top: "70%", right: "5%", delay: "1.5s", duration: "6.5s" },
  { src: "/images/emoji/14-white-blood-cell-1.png", alt: "WBC", size: 60, top: "40%", left: "8%", delay: "2s", duration: "7.5s" },
  { src: "/images/emoji/1-intestines.png", alt: "Intestine", size: 70, top: "25%", right: "3%", delay: "0.8s", duration: "6.8s" },
  { src: "/images/emoji/8-blood-bagcolor.png", alt: "Blood Bag", size: 55, top: "80%", left: "15%", delay: "1.2s", duration: "7.2s" },
  { src: "/images/emoji/7-pill-pack.png", alt: "Pill Pack", size: 60, top: "5%", right: "20%", delay: "2.2s", duration: "6.3s" },
  { src: "/images/emoji/11-scales.png", alt: "Weight Scale", size: 65, top: "85%", right: "15%", delay: "0.3s", duration: "7.8s" },
  { src: "/images/emoji/4-bottom_spine.png", alt: "Spine", size: 85, top: "45%", right: "10%", delay: "1.8s", duration: "6.6s" },
];

const stats = [
  { value: "14", label: "Emoji Proposed" },
  { value: "2", label: "Accepted by Unicode" },
  { value: "10", label: "In Progress" },
  { value: "3.6K+", label: "Emoji Exist Today" },
];

export function Hero() {
  return (
    <section className="relative min-h-[100dvh] overflow-hidden bg-[#0a0a1a]">
      {/* Gradient mesh background */}
      <div className="absolute inset-0">
        <div className="absolute left-1/4 top-1/4 h-[500px] w-[500px] rounded-full bg-[#3452ff]/20 blur-[120px]" />
        <div className="absolute bottom-1/4 right-1/4 h-[400px] w-[400px] rounded-full bg-[#ff1053]/15 blur-[100px]" />
        <div className="absolute left-1/2 top-1/2 h-[600px] w-[600px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-[#ffcf6d]/10 blur-[150px]" />
      </div>

      {/* Subtle grid pattern */}
      <div
        className="absolute inset-0 opacity-[0.03]"
        style={{
          backgroundImage: "linear-gradient(rgba(255,255,255,.1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.1) 1px, transparent 1px)",
          backgroundSize: "60px 60px",
        }}
      />

      {/* Floating emoji */}
      {floatingEmoji.map((emoji) => (
        <div
          key={emoji.alt}
          className="absolute hidden opacity-0 sm:block sm:animate-[heroFloat_var(--dur)_ease-in-out_var(--delay)_infinite_both]"
          style={{
            top: emoji.top,
            left: "left" in emoji ? emoji.left : undefined,
            right: "right" in emoji ? emoji.right : undefined,
            "--delay": emoji.delay,
            "--dur": emoji.duration,
          } as React.CSSProperties}
        >
          <div className="relative drop-shadow-[0_0_20px_rgba(255,207,109,0.3)]">
            <Image
              src={emoji.src}
              alt={emoji.alt}
              width={emoji.size}
              height={emoji.size}
              className="select-none"
              priority
            />
          </div>
        </div>
      ))}

      {/* Content */}
      <div className="relative z-10 flex min-h-[100dvh] flex-col items-center justify-center px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-4xl text-center">
          {/* Badge */}
          <div className="mb-8 inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-white/70 backdrop-blur-sm animate-[fadeInUp_0.6s_ease-out_both]">
            <span className="inline-block h-2 w-2 rounded-full bg-[#ffcf6d] animate-pulse" />
            Advocating for medical emoji since 2019
          </div>

          {/* Main heading */}
          <h1 className="text-5xl font-extrabold tracking-tight sm:text-6xl lg:text-8xl animate-[fadeInUp_0.8s_ease-out_0.1s_both]">
            <span className="text-white">Emoji For</span>
            <br />
            <span className="bg-gradient-to-r from-[#ffcf6d] via-[#ff8a3d] to-[#ff1053] bg-clip-text text-transparent">
              Medicine
            </span>
          </h1>

          {/* Subtext */}
          <p className="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-white/60 sm:text-xl animate-[fadeInUp_0.8s_ease-out_0.3s_both]">
            Over 3,600 emoji exist — almost none represent healthcare.
            We&apos;re proposing new medical emoji to the Unicode Consortium,
            backed by the world&apos;s leading medical societies.
          </p>

          {/* CTA buttons */}
          <div className="mt-10 flex flex-col items-center justify-center gap-4 sm:flex-row animate-[fadeInUp_0.8s_ease-out_0.5s_both]">
            <Link
              href="#candidates"
              className="group inline-flex min-h-[48px] items-center justify-center gap-2 rounded-full bg-gradient-to-r from-[#ffcf6d] to-[#ff8a3d] px-8 py-3 text-base font-semibold text-[#0a0a1a] shadow-lg shadow-[#ffcf6d]/20 transition-all hover:shadow-xl hover:shadow-[#ffcf6d]/30 hover:scale-[1.02]"
            >
              See the Emoji
              <svg className="h-4 w-4 transition-transform group-hover:translate-y-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
              </svg>
            </Link>
            <Link
              href="/campaign"
              className="inline-flex min-h-[48px] items-center justify-center rounded-full border border-white/20 bg-white/5 px-8 py-3 text-base font-semibold text-white backdrop-blur-sm transition-all hover:bg-white/10 hover:border-white/30"
            >
              Join the Campaign
            </Link>
          </div>

          {/* Accepted emoji showcase */}
          <div className="mt-16 flex items-center justify-center gap-3 animate-[fadeInUp_0.8s_ease-out_0.7s_both]">
            <span className="text-sm text-white/40">Already accepted:</span>
            <span className="text-4xl" title="Anatomical Heart">🫀</span>
            <span className="text-4xl" title="Lungs">🫁</span>
            <span className="text-sm text-white/40">Unicode 14.0</span>
          </div>
        </div>

        {/* Stats bar at bottom of hero */}
        <div className="absolute bottom-0 left-0 right-0 border-t border-white/5 bg-white/[0.02] backdrop-blur-md">
          <div className="mx-auto max-w-5xl px-4 py-6 sm:px-6 lg:px-8">
            <div className="grid grid-cols-2 gap-6 md:grid-cols-4">
              {stats.map((stat, i) => (
                <div
                  key={stat.label}
                  className="text-center animate-[fadeInUp_0.6s_ease-out_both]"
                  style={{ animationDelay: `${0.9 + i * 0.1}s` }}
                >
                  <div className="text-2xl font-bold text-[#ffcf6d] sm:text-3xl">
                    {stat.value}
                  </div>
                  <div className="mt-1 text-xs font-medium uppercase tracking-wider text-white/40">
                    {stat.label}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
