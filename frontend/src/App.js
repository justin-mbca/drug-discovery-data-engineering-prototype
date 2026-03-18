import React, { useEffect, useState } from 'react';
import axios from 'axios';


function App() {
  const [cdd, setCdd] = useState('');
  const [mosaic, setMosaic] = useState('');
  const [benchling, setBenchling] = useState('');
  const [bigquery, setBigquery] = useState([]);

  useEffect(() => {
    axios.get('/cdd/data').then(res => setCdd(res.data.cdd));
    axios.get('/mosaic/data').then(res => setMosaic(res.data.mosaic));
    axios.get('/benchling/data').then(res => setBenchling(res.data.benchling));
    axios.get('/bigquery/data').then(res => setBigquery(res.data.bigquery || []));
  }, []);

  return (
    <div>
      <h1>Drug Discovery Data Engineering Prototype</h1>
      <div>CDD Vault: {cdd}</div>
      <div>Mosaic: {mosaic}</div>
      <div>Benchling: {benchling}</div>
      <div>
        <h2>BigQuery Tables in drug_discovery Dataset</h2>
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
