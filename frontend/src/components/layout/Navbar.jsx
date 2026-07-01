import { useState } from "react";
import {
  Search,
  Bell,
  ChevronDown,
  Activity,
} from "lucide-react";
import { useLocation } from "react-router-dom";

const titles = {
  "/assistant": "Enterprise AI Assistant",
  "/dashboard": "Hospital Dashboard",
  "/patients": "Patients",
  "/doctors": "Doctors",
  "/appointments": "Appointments",
  "/admissions": "Admissions",
  "/laboratory": "Laboratory",
  "/billing": "Billing",
  "/analytics": "Analytics",
  "/settings": "Settings",
};

export default function Navbar() {
  const { pathname } = useLocation();

  const [query, setQuery] = useState("");
  const [menuOpen, setMenuOpen] = useState(false);

  const title = titles[pathname] || "Clinical AI";

  return (
    <header className="sticky top-0 z-30 h-24 border-b border-slate-800 bg-[#0f172a]/95 backdrop-blur-xl">

      <div className="flex h-full items-center justify-between px-10 xl:px-16">

        <div>
          <h1 className="text-3xl font-bold text-white tracking-tight">
            {title}
          </h1>

          <div className="mt-2 flex items-center gap-2 text-base text-slate-400">

            <Activity size={16} className="text-green-400" />

            <span>
              Enterprise Clinical Knowledge & Hospital Operations Platform
            </span>

          </div>
        </div>

        <div className="flex items-center gap-5">

          <div className="hidden xl:flex items-center gap-4 w-[600px] rounded-2xl border border-slate-700 bg-slate-900 px-5 py-4">

            <Search
              size={22}
              className="text-slate-500"
            />

            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search patients, doctors, departments, admissions..."
              className="w-full bg-transparent text-base text-white outline-none placeholder:text-slate-500"
            />

          </div>

          <button className="relative flex h-14 w-14 items-center justify-center rounded-2xl border border-slate-700 bg-slate-900 hover:bg-slate-800 transition">

            <Bell size={22} />

            <span className="absolute right-3 top-3 h-2.5 w-2.5 rounded-full bg-red-500" />

          </button>

          <div className="relative">

            <button
              onClick={() => setMenuOpen(!menuOpen)}
              onBlur={() =>
                setTimeout(() => setMenuOpen(false), 150)
              }
              className="flex items-center gap-4 rounded-2xl border border-slate-700 bg-slate-900 px-3 py-2 hover:bg-slate-800 transition"
            >

              <div className="flex h-12 w-12 items-center justify-center rounded-full bg-blue-600 text-lg font-bold text-white">

                HA

              </div>

              <div className="hidden md:block text-left">

                <p className="text-base font-semibold text-white">
                  Enterprise Admin
                </p>

                <p className="text-sm text-slate-400">
                  Hospital Administrator
                </p>

              </div>

              <ChevronDown
                size={18}
                className={`transition ${
                  menuOpen ? "rotate-180" : ""
                }`}
              />

            </button>

          </div>

        </div>

      </div>

    </header>
  );
}