export default function Main() {
  var data = [1, 2, 3, 4, 5];
  return (
    <main className="px-3">
      <h1>Video Preview</h1>
      <div className="row row-cols-3 g-2">
        {data.map((user) => (
          <div className="col">
            <div className="card text-white bg-secondary">
              <div className="card-body">
                <h5 className="card-title">Special title treatment</h5>
                <video
                  src="https://codingyaar.com/wp-content/uploads/video-in-bootstrap-card.mp4"
                  controls
                ></video>
                <a href="/video-tags" className="btn btn-dark">
                  Explore tags
                </a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}
