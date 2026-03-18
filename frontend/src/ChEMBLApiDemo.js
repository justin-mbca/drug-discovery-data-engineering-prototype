import React, { useState } from 'react';
import axios from 'axios';

function ChEMBLApiDemo() {
  const [chemblId, setChemblId] = useState('CHEMBL25'); // Example: Aspirin
  const [compound, setCompound] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchChEMBL = async () => {
    setLoading(true);
    setError(null);
    setCompound(null);
    try {
      const res = await axios.get(
        `https://www.ebi.ac.uk/chembl/api/data/molecule/${chemblId}.json`
      );
      setCompound(res.data);
    } catch (e) {
      setError('Compound not found or API error.');
    }
    setLoading(false);
  };

  return (
    <div style={{marginTop: 40}}>
      <h2>ChEMBL API Demo</h2>
      <div style={{marginBottom: 10}}>
        <label>ChEMBL ID: </label>
        <input value={chemblId} onChange={e => setChemblId(e.target.value)} style={{width: 120}} />
        <button onClick={fetchChEMBL} disabled={loading} style={{marginLeft: 8}}>
          {loading ? 'Loading...' : 'Fetch'}
        </button>
      </div>
      {error && <div style={{color: 'red'}}>{error}</div>}
      {compound && (
        <div style={{marginTop: 20, background: '#f4f4f4', padding: 16, borderRadius: 8}}>
          <strong>ChEMBL ID:</strong> {compound.molecule_chembl_id}<br />
          <strong>Preferred Name:</strong> {compound.pref_name || 'N/A'}<br />
          <strong>Molecule Type:</strong> {compound.molecule_type}<br />
          <pre style={{fontSize: 12, marginTop: 10}}>{JSON.stringify(compound, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default ChEMBLApiDemo;
