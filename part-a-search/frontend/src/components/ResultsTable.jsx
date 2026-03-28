export default function ResultsTable({ results, searched, loading }) {
  if (!searched) {
    return (
      <p style={{ marginTop: 16, opacity: 0.75 }}>
        Use Search, Enter in the form, or change category to load inventory.
      </p>
    )
  }

  if (loading && results.length === 0) {
    return <p style={{ marginTop: 16 }}>Loading…</p>
  }

  if (!loading && results.length === 0) {
    return <p style={{ marginTop: 16 }}>No results found.</p>
  }

  return (
    <div style={{ marginTop: 16 }}>
      {loading && (
        <p style={{ marginBottom: 8, opacity: 0.8 }} aria-live="polite">
          Updating…
        </p>
      )}
      <table width="100%" border="1" cellPadding="8" style={{ borderCollapse: "collapse" }}>
        <thead>
          <tr>
            {/* <th>ID</th> */}
            <th>Name</th>
            <th>Category</th>
            <th>Price (₹)</th>
          </tr>
        </thead>
        <tbody>
          {results.map((item) => (
            <tr key={item.id}>
              {/* <td>{item.id}</td> */}
              <td>{item.name}</td>
              <td>{item.category}</td>
              <td>{Number(item.price).toLocaleString("en-IN")}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
