
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import AnalyticsDashboard from './AnalyticsDashboard';

function App() {
  const [page, setPage] = useState('main');
  const [cdd, setCdd] = useState(null);
  const [mosaic, setMosaic] = useState(null);
  const [benchling, setBenchling] = useState(null);
  const [bigquery, setBigquery] = useState([]);

  useEffect(() => {
    const nocache = '?nocache=' + Date.now();
    axios.get('/cdd/data' + nocache).then(res => setCdd(res.data.cdd));
    axios.get('/mosaic/data' + nocache).then(res => setMosaic(res.data.mosaic));
    axios.get('/benchling/data' + nocache).then(res => setBenchling(res.data.benchling));
    axios.get('/bigquery/data' + nocache).then(res => setBigquery(res.data.bigquery || []));
  }, []);

  if (page === 'analytics') {
    return (
      <div>
        <button onClick={() => setPage('main')}>Back to Main</button>
        <AnalyticsDashboard />
      </div>
    );
  }

  return (
    <div>
      <h1>Drug Discovery Data Engineering Prototype</h1>
      <button onClick={() => setPage('analytics')} style={{marginBottom: 20}}>Go to ETL & Analytics Dashboard</button>
      <div>
        <strong>CDD Vault:</strong> {cdd && typeof cdd === 'object' ? (
          <span>
            Compound: {cdd.compound_id}, Name: {cdd.name}, Activity: {cdd.activity}, Project: {cdd.project}
          </span>
        ) : ''}
      </div>
      <div>
        <strong>Mosaic:</strong> {mosaic && typeof mosaic === 'object' ? (
          <span>
            Sample: {mosaic.sample_id}, Location: {mosaic.location}, Quantity: {mosaic.quantity}{mosaic.unit}, Status: {mosaic.status}
          </span>
        ) : ''}
      </div>
      <div>
        <strong>Benchling:</strong> {benchling && typeof benchling === 'object' ? (
          <span>
            Entry: {benchling.entry_id}, Experiment: {benchling.experiment}, Scientist: {benchling.scientist}, Result: {benchling.result}
          </span>
        ) : ''}
      </div>
      <div>
        <h2>BigQuery Tables in drug_discovery Dataset</h2>
        <div style={{fontSize: '0.95em', color: '#555', marginBottom: 8}}>
          <b>Note:</b> These tables are populated by ETL from CDD Vault, Mosaic, and Benchling. In demo mode, data is mocked; in production, these would be real BigQuery tables.
        </div>
        {bigquery.length === 0 ? (
          <div>No tables found.</div>
        ) : (
          <ul>
            {bigquery.map((row, idx) => (
              <li key={idx}>{row.table_schema}.{row.table_name}</li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default App;
