import { FileText, Tag, ArrowUpRight } from "lucide-react";

export default function SourceCard({
  document,
  page,
  category,
}) {
  return (
    <div className="group w-[340px] rounded-2xl border border-slate-700 bg-slate-900 hover:border-blue-500 hover:bg-slate-800 transition-all duration-300 cursor-pointer">

      <div className="flex items-start gap-4 p-5">

        <div className="w-12 h-12 rounded-xl bg-blue-600/15 flex items-center justify-center shrink-0">
          <FileText size={22} className="text-blue-400" />
        </div>

        <div className="flex-1">

          <h3 className="text-base font-semibold text-white leading-6">
            {document}
          </h3>

          <div className="flex items-center gap-3 mt-4">

            {page !== undefined && (
              <span className="rounded-lg bg-slate-800 px-3 py-1 text-sm text-slate-300">
                📄 Page {page}
              </span>
            )}

            {category && (
              <span className="flex items-center gap-1 rounded-lg bg-blue-600/20 px-3 py-1 text-sm text-blue-300">
                <Tag size={14} />
                {category}
              </span>
            )}

          </div>

        </div>

        <ArrowUpRight
          size={18}
          className="text-slate-500 group-hover:text-blue-400 transition-colors"
        />

      </div>

    </div>
  );
}