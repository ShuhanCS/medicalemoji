import { Hero } from "@/components/Hero";
import { EmojiGrid } from "@/components/EmojiGrid";
import { Timeline } from "@/components/Timeline";
import { ContactForm } from "@/components/ContactForm";
import { pressMentions } from "@/data/press";

function StatsBar() {
  const stats = [
    { label: "Emoji Proposed", value: "14" },
    { label: "Accepted", value: "2" },
    { label: "In Progress", value: "10" },
    { label: "New", value: "2" },
  ];

  return (
    <section className="border-y border-gray-100 bg-white">
      <div className="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
        <div className="grid grid-cols-2 gap-6 md:grid-cols-4">
          {stats.map((stat) => (
            <div key={stat.label} className="text-center">
              <div className="text-3xl font-extrabold text-gray-900 sm:text-4xl">
                {stat.value}
              </div>
              <div className="mt-1 text-sm font-medium text-gray-500">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function OurStory() {
  return (
    <section className="bg-white py-20" id="story">
      <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            Our Story
          </h2>
        </div>
        <div className="mt-8 space-y-6 text-lg leading-relaxed text-gray-600">
          <p>
            In 2019, <strong className="text-gray-900">Shuhan He, MD</strong> and{" "}
            <strong className="text-gray-900">Jenny 8 Lee</strong> teamed up with members of{" "}
            <strong className="text-gray-900">Emojination</strong> to submit the anatomical heart
            and lungs emoji to the Unicode Consortium.
          </p>
          <p>
            Their effort was motivated by a simple observation: with over 3,600 emoji in the
            Unicode standard, almost none represented the human body, medical conditions, or
            healthcare tools that billions of people interact with every day.
          </p>
          <p>
            The anatomical heart and lungs were officially accepted into Unicode 14.0 in 2021,
            appearing on billions of devices worldwide. This success, documented in a{" "}
            <strong className="text-gray-900">JAMA</strong> article, proved that the medical
            community could successfully advocate for better emoji representation.
          </p>
          <p>
            Now, the Medical Emoji team has grown and is working to propose additional medical
            emoji &mdash; from organs like the kidney and liver to tools like the EKG and blood
            bag &mdash; to ensure medicine is fully represented in our digital communication.
          </p>
        </div>
      </div>
    </section>
  );
}

function WhyMedicalEmoji() {
  return (
    <section className="bg-white py-20" id="why">
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            Why Medical Emoji?
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-lg text-gray-600">
            Emoji are more than decoration &mdash; they&apos;re a universal language. Medical emoji
            can improve communication between patients and providers.
          </p>
        </div>

        <div className="mt-12 grid gap-8 md:grid-cols-2">
          {/* Before */}
          <div className="rounded-2xl border border-gray-100 bg-gray-50 p-8">
            <div className="mb-4 inline-flex rounded-full bg-gray-200 px-3 py-1 text-xs font-semibold uppercase tracking-wider text-gray-600">
              Before
            </div>
            <h3 className="text-xl font-semibold text-gray-900">
              Without Medical Emoji
            </h3>
            <p className="mt-3 text-gray-600">
              Patients struggle to express symptoms and conditions in text messages, telehealth
              chats, and social media. Generic emoji like a red circle or sad face fail to convey
              specific medical meaning.
            </p>
            <div className="mt-4 flex items-center gap-3 text-3xl">
              <span>😟</span>
              <span>🔴</span>
              <span>💊</span>
              <span className="text-base text-gray-400">= vague</span>
            </div>
          </div>

          {/* After */}
          <div className="rounded-2xl border border-[#3452ff]/20 bg-[#3452ff]/5 p-8">
            <div className="mb-4 inline-flex rounded-full bg-gradient-to-r from-[#3452ff] to-[#ff1053] px-3 py-1 text-xs font-semibold uppercase tracking-wider text-white">
              After
            </div>
            <h3 className="text-xl font-semibold text-gray-900">
              With Medical Emoji
            </h3>
            <p className="mt-3 text-gray-600">
              Specific medical emoji like the anatomical heart, lungs, kidney, and EKG allow
              precise, instant communication about health conditions. Visual Analogue Scales using
              emoji help quantify pain.
            </p>
            <div className="mt-4 flex items-center gap-3 text-3xl">
              <span>🫀</span>
              <span>🫁</span>
              <span>🩺</span>
              <span className="text-base text-[#3452ff]">= precise</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function PressSection() {
  return (
    <section className="bg-gray-50 py-20" id="press">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            In the Press
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-lg text-gray-600">
            Our work has been featured in leading medical journals and major media outlets.
          </p>
        </div>

        <div className="mt-12 grid grid-cols-2 gap-4 sm:grid-cols-3 sm:gap-6 md:grid-cols-4 lg:grid-cols-7">
          {pressMentions.map((mention) => (
            <a
              key={mention.outlet}
              href={mention.url}
              target="_blank"
              rel="noopener noreferrer"
              className="flex flex-col items-center justify-center rounded-2xl border border-gray-100 bg-white p-4 shadow-sm transition-all hover:-translate-y-1 hover:shadow-md sm:p-6"
              title={mention.title}
            >
              <div className="flex h-12 items-center justify-center">
                <span className="text-center text-sm font-bold text-gray-700">{mention.outlet}</span>
              </div>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}

function ContactSection() {
  return (
    <section className="bg-gradient-to-r from-[#3452ff] to-[#ff1053] py-20" id="contact">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h2 className="text-3xl font-bold tracking-tight text-white sm:text-4xl">
            Get in Touch
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-lg text-white/80">
            Want to support the medical emoji campaign? Have questions or ideas? We&apos;d love to
            hear from you.
          </p>
        </div>
        <div className="mt-10">
          <ContactForm variant="gradient" />
        </div>
      </div>
    </section>
  );
}

export default function Home() {
  return (
    <>
      <Hero />
      <StatsBar />
      <EmojiGrid />
      <OurStory />
      <Timeline />
      <WhyMedicalEmoji />
      <PressSection />
      <ContactSection />
    </>
  );
}
