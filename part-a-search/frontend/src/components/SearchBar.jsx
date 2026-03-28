const CATEGORIES = ["", "Electronics", "Furniture", "Stationery"]

/** Reads live DOM values (reliable with controlled inputs; FormData can lag or omit). */
function snapshotFromForm(form) {
  const v = (name) => {
    const el = form.elements.namedItem(name)
    if (!el || !("value" in el)) return ""
    return String(el.value ?? "")
  }
  return {
    q: v("q"),
    category: v("category"),
    minPrice: v("minPrice"),
    maxPrice: v("maxPrice"),
  }
}

export default function SearchBar({ filters, setFilters, onSearch }) {
  function handleChange(e) {
    setFilters((prev) => ({ ...prev, [e.target.name]: e.target.value }))
  }

  function handleSubmit(e) {
    e.preventDefault()
    const snap = snapshotFromForm(e.currentTarget)
    setFilters(snap)
    onSearch(snap)
  }

  function handleCategoryChange(e) {
    const form = e.target.form
    if (!form) return
    const snap = snapshotFromForm(form)
    setFilters(snap)
    onSearch(snap)
  }

  return (
    <form
      noValidate
      onSubmit={handleSubmit}
      style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: 24 }}
    >
      <input
        name="q"
        placeholder="Search product..."
        value={filters.q}
        onChange={handleChange}
      />

      <select name="category" value={filters.category} onChange={handleCategoryChange}>
        {CATEGORIES.map((c) => (
          <option key={c} value={c}>
            {c || "All Categories"}
          </option>
        ))}
      </select>

      <input
        name="minPrice"
        type="number"
        placeholder="Min price"
        value={filters.minPrice}
        onChange={handleChange}
      />

      <input
        name="maxPrice"
        type="number"
        placeholder="Max price"
        value={filters.maxPrice}
        onChange={handleChange}
      />

      <button type="submit">Search</button>
    </form>
  )
}
