import React, { useState } from 'react';
import axios from 'axios';

// Set axios base URL for all API requests (configurable for local/cloud)
axios.defaults.baseURL = process.env.REACT_APP_API_URL || 'https://drug-discovery-data-engineering-prototype.onrender.com';


function AnalyticsDashboard() {
  // Info modal state
  const [showInfo, setShowInfo] = useState(false);
  const [etlStatus, setEtlStatus] = useState('');
  const [tables, setTables] = useState(null);
  const [summary, setSummary] = useState(null);
  const [selectedTable, setSelectedTable] = useState('');
  const [tableRows, setTableRows] = useState([]);
  const [loading, setLoading] = useState(false);
  const [availableCompounds, setAvailableCompounds] = useState(null);
  const [experimentsByCompound, setExperimentsByCompound] = useState(null);

  const runEtl = async () => {
    setLoading(true);
    setEtlStatus('Running ETL...');
    try {
      await axios.post('/mock/etl/run');
      setEtlStatus('ETL complete!');
    } catch (e) {
      setEtlStatus('ETL failed.');
    }
    setLoading(false);
    fetchTables();
    fetchSummary();
  };

  const fetchTables = async () => {
    const res = await axios.get('/mock/etl/tables');
    setTables(res.data);
  };

  const fetchSummary = async () => {
    const res = await axios.get('/mock/etl/analytics/summary');
    setSummary(res.data);
  };

  const fetchTableRows = async (table) => {
    setSelectedTable(table);
    const res = await axios.get(`/mock/etl/table/${table}`);
    setTableRows(res.data.rows || []);
  };

  const fetchAvailableCompounds = async () => {
    const res = await axios.get('/mock/etl/analytics/available_compounds');
    setAvailableCompounds(res.data.available_compounds || []);
  };

  const fetchExperimentsByCompound = async () => {
    const res = await axios.get('/mock/etl/analytics/experiments_by_compound');
    setExperimentsByCompound(res.data.experiments_by_compound || {});
  };

  return (
    <div style={{marginTop: 40}}>
      <h2>ETL & Analytics Dashboard</h2>
      <button onClick={() => setShowInfo(true)} style={{float: 'right', marginTop: -35}}>Info</button>
      {showInfo && (
        <div style={{background: '#fff', border: '1px solid #888', borderRadius: 8, padding: 20, position: 'fixed', top: 80, left: '50%', transform: 'translateX(-50%)', zIndex: 1000, maxWidth: 500}}>
          <h3>About This Dashboard</h3>
          <ul>
            <li>This dashboard demonstrates ETL and analytics for drug discovery data.</li>
            <li>Data sources: <b>CDD Vault</b> (compounds), <b>Mosaic</b> (samples), <b>Benchling</b> (experiments).</li>
            <li>ETL loads data from these sources into <b>BigQuery</b> tables: <code>cdd</code>, <code>mosaic</code>, <code>benchling</code>.</li>
            <li>In demo mode, data is mocked in-memory. In production, the backend can connect to real BigQuery tables using GCP credentials.</li>
            <li>You can switch between mock and real BigQuery connections in the backend (see README for details).</li>
          </ul>
          <button onClick={() => setShowInfo(false)} style={{marginTop: 10}}>Close</button>
        </div>
      )}
      <button onClick={runEtl} disabled={loading} style={{marginBottom: 10}}>
        {loading ? 'Running ETL...' : 'Run ETL (Load Mock Data)'}
      </button>
      {loading && (
        <div style={{ color: '#1976d2', fontWeight: 'bold', marginBottom: 10 }}>Running ETL, please wait...</div>
      )}
      <div>{etlStatus}</div>
      <div style={{marginTop: 20}}>
        <button onClick={fetchTables}>Show Mock Tables</button>
        {tables && (
          <ul>
            {Object.entries(tables).map(([name, count]) => (
              <li key={name}>
                <button onClick={() => fetchTableRows(name)}>{name}</button>: {count} rows
              </li>
            ))}
          </ul>
        )}
      </div>
      <div style={{marginTop: 20}}>
        <button onClick={fetchSummary}>Show Analytics Summary</button>
        {summary && (
          <div>
            <strong>Summary:</strong>
            <ul>
              <li>CDD rows: {summary.cdd_count}</li>
              <li>Mosaic rows: {summary.mosaic_count}</li>
              <li>Benchling rows: {summary.benchling_count}</li>
            </ul>
          </div>
        )}
      </div>
      <div style={{marginTop: 20}}>
        <button onClick={fetchAvailableCompounds}>Show Available Compounds (Join CDD & Mosaic)</button>
        {availableCompounds && (
          <div>
            <strong>Available Compounds:</strong>
            <ul>
              {availableCompounds.map((row, idx) => (
                <li key={idx}>
                  Compound: {row.compound_name} (ID: {row.compound_id}), Sample: {row.sample_id}, Location: {row.location}, Quantity: {row.quantity}{row.unit}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
      <div style={{marginTop: 20}}>
        <button onClick={fetchExperimentsByCompound}>Show Experiments by Compound (Benchling)</button>
        {experimentsByCompound && (
          <div>
            <strong>Experiments by Compound:</strong>
            <ul>
              {Object.entries(experimentsByCompound).map(([cid, exps]) => (
                <li key={cid}>
                  <strong>Compound ID: {cid}</strong>
                  <ul>
                    {exps.map((exp, i) => (
                      <li key={i}>
                        {exp.experiment} ({exp.date}) by {exp.scientist}: {exp.result}
                      </li>
                    ))}
                  </ul>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
      <div style={{marginTop: 20}}>
        {selectedTable && (
          <div>
            <h3>Rows in {selectedTable}</h3>
            {tableRows.length > 0 ? (
              <table style={{ borderCollapse: 'collapse', width: '100%', background: '#f4f4f4' }}>
                <thead>
                  <tr>
                    {Object.keys(tableRows[0]).map((col) => (
                      <th key={col} style={{ border: '1px solid #ccc', padding: '4px', background: '#e0e0e0' }}>{col}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {tableRows.map((row, idx) => (
                    <tr key={idx}>
                      {Object.values(row).map((val, i) => (
                        <td key={i} style={{ border: '1px solid #ccc', padding: '4px' }}>{String(val)}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <div style={{background: '#f4f4f4', padding: 10}}>No rows found.</div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default AnalyticsDashboard;
