export default function Navbar() {
  return (
    <header className="mb-auto">
      <nav className="navbar navbar-dark bg-dark">
        <div className="container-fluid">
          <h3 className="float-md-start mb-0">
            <a href="/">
              <img className="m-2" src="logo_unsa.png" width="60px" />
            </a>
            VDprocessing
          </h3>
          <form className="d-flex">
            <input
              className="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button className="btn btn-outline-light m-1" type="submit">
              Search
            </button>
          </form>
        </div>
      </nav>
    </header>
  );
}
