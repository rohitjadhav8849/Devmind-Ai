import { useState } from "react";
import api from "../services/api";

function UploadBox() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a PDF.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await api.post("/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setStatus(res.data.status);
    } catch (err) {
      console.error(err);
      setStatus("Upload failed.");
    }
  };

  return (
    <div className="upload-card">

      <h3>Upload Document</h3>

      <div className="upload-controls">

        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <button onClick={handleUpload}>
          Upload
        </button>

      </div>

      {file && (
        <p className="selected-file">
          Selected: <strong>{file.name}</strong>
        </p>
      )}

      {status && (
        <p className="upload-status">
          {status}
        </p>
      )}

    </div>
  );
}

export default UploadBox;