import $ from "jquery";
import React, { useRef } from "react";
export default function Video() {
  var vidRef = useRef(null);
  var data = [0, 6.6, 24.7, 42.3];

  function skipTime(time) {
    vidRef.current.play();
    vidRef.current.pause();
    vidRef.current.currentTime = time;
    vidRef.current.play();
  }
  function changeCurrentTime(e) {
    $(".vidchaNav>*").addClass("list-group-item-dark");
    e.currentTarget.classList.remove("list-group-item-dark");
    e.currentTarget.classList.add("list-group-item-light");
    skipTime(e.currentTarget.dataset.start);
  }
  return (
    <main className="px-3">
      <div className="row">
        <div className="col-8">
          <div className="card text-white bg-secondary m-1">
            <div className="card-body">
              <h3 className="card-title">Special title treatment</h3>
              <video
                ref={vidRef}
                className="vidchaVideo"
                src="videos/explore.mp4"
                controls
              ></video>
            </div>
          </div>
        </div>
        <div className="col-4">
          <div className="card text-white bg-secondary m-1">
            <div className="card-body">
              <h5 className="card-title">Tags Found</h5>
              <ul className="vidchaNav list-group list-group-numbered">
                {data.map((item) => (
                  <li
                    key={item}
                    onClick={changeCurrentTime}
                    data-start={item}
                    className="list-group-item list-group-item-dark"
                  >
                    An item
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
