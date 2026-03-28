import { useState, useEffect, useCallback, useRef } from "react"

import ResultsTable from "./components/ResultsTable"
import SearchBar from "./components/searchBar"

/** Dev: proxied by Vite (vite.config.js) so CORS / localhost vs 127.0.0.1 does not break fetch */
const SEARCH_URL = "/search"

function filtersFromLocation() {
  if (typeof window === "undefined") {
    return { q: "", category: "", minPrice: "", maxPrice: "" }
  }
  const p = new URLSearchParams(window.location.search)
  return {
    q: p.get("q") ?? "",
    category: p.get("category") ?? "",
    minPrice: p.get("minPrice") ?? "",
    maxPrice: p.get("maxPrice") ?? "",
  }
}

export default function App() {
  const [filters, setFilters] = useState(filtersFromLocation)
  const [results, setResults] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [searched, setSearched] = useState(false)

  const filtersRef = useRef(filters)
  filtersRef.current = filters

  const handleSearch = useCallback(async (f) => {
    const snap = f ?? filtersRef.current
    setLoading(true)
    setError(null)

    const params = new URLSearchParams()
    if (snap.q) params.append("q", snap.q)
    if (snap.category) params.append("category", snap.category)
    if (snap.minPrice) params.append("minPrice", snap.minPrice)
    if (snap.maxPrice) params.append("maxPrice", snap.maxPrice)

    const qs = params.toString()
    window.history.replaceState(null, "", qs ? `${window.location.pathname}?${qs}` : window.location.pathname)

    try {
      const res = await fetch(qs ? `${SEARCH_URL}?${qs}` : SEARCH_URL)
      const data = await res.json().catch(() => ({}))
      if (!res.ok) {
        throw new Error(data.message || "Invalid filters or server error")
      }
      setResults(data.products ?? [])
      setSearched(true)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    const p = new URLSearchParams(window.location.search)
    if (!p.toString()) return
    handleSearch(filtersFromLocation())
  }, [handleSearch])

  return (
    <div
      style={{
        maxWidth: 800,
        margin: "0 auto",
        padding: "0 16px 40px",
        textAlign: "left",
        width: "100%",
        boxSizing: "border-box",
      }}
    >
      <h1 style={{ textAlign: "center" }}>Inventory Search</h1>
      <SearchBar filters={filters} setFilters={setFilters} onSearch={handleSearch} />
      {error && (
        <p style={{ color: "red", marginTop: 12 }} role="alert">
          {error}
        </p>
      )}
      <ResultsTable results={results} searched={searched} loading={loading} />
    </div>
  )
}
