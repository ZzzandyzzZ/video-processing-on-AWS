import $ from "jquery";
import "react-dropzone-uploader/dist/styles.css";
import Dropzone from "react-dropzone-uploader";
const fileTypes = ["wmv", "mov", "mp4", "avi", "3gp"];
export default function Video() {
  const getUploadParams = ({ meta }) => {
    const url = "https://httpbin.org/post";
    return {
      url,
      meta: { fileUrl: `${url}/${encodeURIComponent(meta.name)}` },
    };
  };

  const handleChangeStatus = ({ meta }, status) => {
    console.log(status, meta);
  };

  const handleSubmit = (files, allFiles) => {
    files.map((f) =>
      fetch("http://localhost:5000/upload", {
        method: "POST",
        body: f,
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      })
        .catch((error) => alert("Hubo un error, intentelo de nuevo"))
        .then(function (response) {
          console.log(response);
        })
    );
    allFiles.forEach((f) => f.remove());
  };
  return (
    <main className="px-3">
      <div className="card text-white bg-secondary m-1">
        <Dropzone
          getUploadParams={getUploadParams}
          onChangeStatus={handleChangeStatus}
          onSubmit={handleSubmit}
          accept="video/*"
          canCancel={true}
          maxFiles={1}
          inputContent={(files, extra) =>
            extra.reject
              ? "Image, audio and video files only"
              : "Select or drag you video"
          }
          styles={{
            dropzoneReject: { borderColor: "red", backgroundColor: "#DAA" },
            inputLabel: (files, extra) =>
              extra.reject ? { color: "red" } : {},
          }}
        />
      </div>
    </main>
  );
}
