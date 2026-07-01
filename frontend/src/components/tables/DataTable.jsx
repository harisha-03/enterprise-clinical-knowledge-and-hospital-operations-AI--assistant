import { useMemo, useState } from 'react'
import { Search, ChevronLeft, ChevronRight } from 'lucide-react'
import Badge, { statusVariant } from '../ui/Badge.jsx'

const PAGE_SIZE = 8

/**
 * Generic data table.
 * columns: [{ key, label, render?(row) }]
 * data: array of row objects (must include `status` if statusKey used)
 */
export default function DataTable({ columns, data, searchKeys = [], filters = [] }) {
  const [query, setQuery] = useState('')
  const [activeFilter, setActiveFilter] = useState('All')
  const [page, setPage] = useState(1)

  const filtered = useMemo(() => {
    let rows = data
    if (activeFilter !== 'All') {
      rows = rows.filter((r) => r.department === activeFilter || r.status === activeFilter || r.ward === activeFilter)
    }
    if (query.trim()) {
      const q = query.toLowerCase()
      rows = rows.filter((r) => searchKeys.some((k) => String(r[k]).toLowerCase().includes(q)))
    }
    return rows
  }, [data, query, activeFilter, searchKeys])

  const totalPages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE))
  const pageRows = filtered.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE)

  function changePage(next) {
    setPage(Math.min(Math.max(next, 1), totalPages))
  }

  return (
    <div>
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 px-6 pt-6 pb-4">
        <div className="flex items-center gap-2.5 bg-bg border border-border rounded-xl px-4 py-2.5 w-full sm:w-80">
          <Search size={15} className="text-subtle" />
          <input
            value={query}
            onChange={(e) => { setQuery(e.target.value); setPage(1) }}
            placeholder="Search..."
            className="bg-transparent outline-none text-sm text-slate-200 placeholder:text-subtle w-full"
          />
        </div>
        {filters.length > 0 && (
          <div className="flex flex-wrap items-center gap-1.5">
            {['All', ...filters].map((f) => (
              <button
                key={f}
                onClick={() => { setActiveFilter(f); setPage(1) }}
                className={`px-2.5 py-1 rounded-full text-xs font-medium border transition-colors ${
                  activeFilter === f
                    ? 'bg-primary/15 text-primary-light border-primary/30'
                    : 'bg-transparent text-subtle border-border hover:text-slate-200'
                }`}
              >
                {f}
              </button>
            ))}
          </div>
        )}
      </div>

      <div className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-y border-border text-left">
              {columns.map((col) => (
                <th key={col.key} className="px-6 py-3 text-sm font-medium text-subtle whitespace-nowrap">
                  {col.label}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {pageRows.map((row, i) => (
              <tr key={row.id ?? i} className="border-b border-border/60 hover:bg-white/[0.02] transition-colors">
                {columns.map((col) => (
                  <td key={col.key} className="px-6 py-4 text-[15px] text-slate-300 whitespace-nowrap">
                    {col.render
                      ? col.render(row)
                      : col.key === 'status'
                        ? <Badge variant={statusVariant(row.status)}>{row.status}</Badge>
                        : row[col.key]}
                  </td>
                ))}
              </tr>
            ))}
            {pageRows.length === 0 && (
              <tr>
                <td colSpan={columns.length} className="px-6 py-12 text-center text-subtle text-base">
                  No records match your search.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      <div className="flex items-center justify-between px-6 py-4 border-t border-border">
        <p className="text-sm text-subtle">
          Showing {pageRows.length === 0 ? 0 : (page - 1) * PAGE_SIZE + 1}-{Math.min(page * PAGE_SIZE, filtered.length)} of {filtered.length}
        </p>
        <div className="flex items-center gap-1.5">
          <button
            onClick={() => changePage(page - 1)}
            disabled={page === 1}
            className="w-7 h-7 flex items-center justify-center rounded-md border border-border text-subtle hover:text-slate-200 hover:bg-white/5 disabled:opacity-40 disabled:hover:bg-transparent"
          >
            <ChevronLeft size={14} />
          </button>
          <span className="text-xs text-muted px-1">{page} / {totalPages}</span>
          <button
            onClick={() => changePage(page + 1)}
            disabled={page === totalPages}
            className="w-7 h-7 flex items-center justify-center rounded-md border border-border text-subtle hover:text-slate-200 hover:bg-white/5 disabled:opacity-40 disabled:hover:bg-transparent"
          >
            <ChevronRight size={14} />
          </button>
        </div>
      </div>
    </div>
  )
}
