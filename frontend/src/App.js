
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import AnalyticsDashboard from './AnalyticsDashboard';
import Overview from './Overview';
import PublicApiDemo from './PublicApiDemo';

function App() {
  const [page, setPage] = useState('overview');
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

  return (
    <div>
      <h1>Drug Discovery Data Engineering Prototype</h1>
      <div style={{marginBottom: 24, marginTop: 16}}>
        <button onClick={() => setPage('overview')} style={{marginRight: 12, fontWeight: page === 'overview' ? 'bold' : 'normal'}}>Overview</button>
        <button onClick={() => setPage('analytics')} style={{marginRight: 12, fontWeight: page === 'analytics' ? 'bold' : 'normal'}}>ETL & Analytics Dashboard</button>
        <button onClick={() => setPage('publicapi')} style={{fontWeight: page === 'publicapi' ? 'bold' : 'normal'}}>Public Data API Demo</button>
      </div>
      {page === 'overview' && <Overview />}
      {page === 'analytics' && <AnalyticsDashboard />}
      {page === 'publicapi' && <PublicApiDemo />}
    </div>
  );
}

export default App;
