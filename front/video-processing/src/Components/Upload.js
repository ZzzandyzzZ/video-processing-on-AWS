import "react-dropzone-uploader/dist/styles.css";
import $ from "jquery";

export default function Video() {
  function handleSubmit(e) {
    e.preventDefault();
    var formData = new FormData(e.currentTarget);
    console.log(formData);
    fetch(e.target.action, {
      method: "POST",
      body: formData,
      headers: { "content-type": "multipart/form-data" },
    })
      .then((resp) => {
        return resp.json();
      })
      .then((body) => {
        alert("Video subido correctamente!");
      })
      .catch((error) => {
        alert("Error al subir video!");
        console.log(error);
      });
  }
  return (
    <main className="px-3">
      <div className="card text-white bg-secondary m-1">
        <iframe
          name="dummyframe"
          id="dummyframe"
          style={{ display: "none" }}
        ></iframe>
        <form
          action="http://localhost:5000/upload"
          method="post"
          encType="multipart/form-data"
          className="input-group p-2"
          id="videofm"
          target="dummyframe"
        >
          <input className="form-control" type="file" name="file" />
          <input
            className="btn btn-outline-dark"
            type="submit"
            value="Upload"
          />
        </form>
      </div>
    </main>
  );
}
