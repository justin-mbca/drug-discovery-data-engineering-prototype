import React from 'react';

export default function Overview() {
  return (
    <div style={{marginTop: 40, maxWidth: 800, marginLeft: 'auto', marginRight: 'auto'}}>
      <h2>System Overview</h2>
      <p>
        This prototype demonstrates a modern data engineering workflow for drug discovery, integrating multiple laboratory informatics systems with a cloud data warehouse and analytics dashboard.
      </p>
      <h3>Workflow Steps</h3>
      <ol>
        <li><b>Data Sources:</b> CDD Vault (compounds), Mosaic (samples), Benchling (experiments).</li>
        <li><b>ETL Process:</b> Data is extracted from each source, transformed, and loaded into BigQuery tables (<code>cdd</code>, <code>mosaic</code>, <code>benchling</code>).</li>
        <li><b>Backend API:</b> A FastAPI service exposes endpoints for ETL, analytics, and direct BigQuery queries.</li>
        <li><b>Frontend UI:</b> A React dashboard allows users to run ETL, view tables, and explore analytics.</li>
        <li><b>Modes:</b> The system can run in <b>mock/demo</b> mode (in-memory data) or connect to <b>real BigQuery</b> for production.</li>
      </ol>
      <h3>Architecture Diagram</h3>
      <img src="/ETLArchitecture.png" alt="Architecture Diagram" style={{width: '100%', border: '1px solid #ccc', borderRadius: 8}} />
      <h3>Key Features</h3>
      <ul>
        <li>End-to-end data flow from lab systems to analytics</li>
        <li>Switchable between mock and real BigQuery connections</li>
        <li>Modern stack: FastAPI, React, Docker, GCP</li>
        <li>Clear separation of ETL, analytics, and UI layers</li>
      </ul>
      <p style={{marginTop: 20, color: '#888'}}>See the README for more technical details and setup instructions.</p>
    </div>
  );
}
