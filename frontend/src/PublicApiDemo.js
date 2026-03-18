import React, { useState } from 'react';
import axios from 'axios';
import ChEMBLApiDemo from './ChEMBLApiDemo';


function PublicApiDemo() {
  const [pubchemCid, setPubchemCid] = useState('2244'); // Example: Aspirin
  const [pubchemCompound, setPubchemCompound] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [chemblId, setChemblId] = useState('CHEMBL25');
  const [chemblCompound, setChemblCompound] = useState(null);
  const [chemblLoading, setChemblLoading] = useState(false);
  const [chemblError, setChemblError] = useState(null);

  const fetchPubChem = async () => {
    setLoading(true);
    setError(null);
    setPubchemCompound(null);
    try {
      const res = await axios.get(
        `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/${pubchemCid}/JSON`
      );
      setPubchemCompound(res.data.PC_Compounds ? res.data.PC_Compounds[0] : null);
    } catch (e) {
      setError('Compound not found or API error.');
    }
    setLoading(false);
  };

  const fetchChEMBL = async () => {
    setChemblLoading(true);
    setChemblError(null);
    setChemblCompound(null);
    try {
      const res = await axios.get(
        `https://www.ebi.ac.uk/chembl/api/data/molecule/${chemblId}.json`
      );
      setChemblCompound(res.data);
    } catch (e) {
      setChemblError('Compound not found or API error.');
    }
    setChemblLoading(false);
  };

  // Simple analytics: compare atom counts if both compounds are loaded
  let analytics = null;
  if (pubchemCompound && chemblCompound) {
    const pubchemAtoms = pubchemCompound.atoms?.aid?.length || 0;
    const chemblAtoms = chemblCompound.molecule_structures?.canonical_smiles ? chemblCompound.molecule_structures.canonical_smiles.length : 0;
    analytics = (
      <div style={{marginTop: 24, background: '#e3f2fd', padding: 12, borderRadius: 8}}>
        <strong>Simple Analytics:</strong><br />
        PubChem Atoms: {pubchemAtoms}<br />
        ChEMBL SMILES Length: {chemblAtoms}<br />
        {pubchemAtoms && chemblAtoms ? (
          <span>
            Ratio (PubChem Atoms / ChEMBL SMILES Length): {(pubchemAtoms / chemblAtoms).toFixed(2)}
          </span>
        ) : null}
      </div>
    );
  }

  return (
    <div style={{marginTop: 40}}>
      <h2>Public Data API Demo</h2>
      <div style={{marginBottom: 16, background: '#e8f5e9', padding: 14, borderRadius: 8, fontSize: 15}}>
        <strong>Purpose:</strong> This demo compares compound data from two major public chemical databases—PubChem and ChEMBL—using their live APIs. It illustrates how the same molecule (e.g., Aspirin) can be represented differently across sources, and demonstrates integration, harmonization, and side-by-side analysis of external scientific data. This is a common real-world task in drug discovery data engineering.
      </div>
      <div style={{
        marginBottom: 24,
        display: 'flex',
        gap: 24,
        flexWrap: 'wrap',
        alignItems: 'flex-start',
        justifyContent: 'flex-start',
      }}>
        <div style={{flex: '0 0 50%', maxWidth: '50%', minWidth: 280, boxSizing: 'border-box'}}>
          <h3>PubChem</h3>
          <label>Compound CID: </label>
          <input value={pubchemCid} onChange={e => setPubchemCid(e.target.value)} style={{width: 100}} />
          <button onClick={fetchPubChem} disabled={loading} style={{marginLeft: 8}}>
            {loading ? 'Loading...' : 'Fetch'}
          </button>
          {error && <div style={{color: 'red'}}>{error}</div>}
          {pubchemCompound && (
            <div style={{marginTop: 10, background: '#f4f4f4', padding: 12, borderRadius: 8, width: '100%', boxSizing: 'border-box', overflowX: 'auto'}}>
              <strong>CID:</strong> {pubchemCid}<br />
              <strong>Title:</strong> {pubchemCompound.props?.[0]?.value?.sval || 'N/A'}<br />
              <strong>Atoms:</strong> {pubchemCompound.atoms?.aid?.length || 'N/A'}<br />
              <strong>Bonds:</strong> {pubchemCompound.bonds?.aid1?.length || 'N/A'}<br />
              <pre style={{fontSize: 12, marginTop: 10, width: '100%', maxWidth: '100%', overflowX: 'auto', whiteSpace: 'pre', wordBreak: 'break-all'}}>{JSON.stringify(pubchemCompound, null, 2)}</pre>
            </div>
          )}
        </div>
        <div style={{flex: '0 0 50%', maxWidth: '50%', minWidth: 280, boxSizing: 'border-box'}}>
          <h3>ChEMBL</h3>
          <label>ChEMBL ID: </label>
          <input value={chemblId} onChange={e => setChemblId(e.target.value)} style={{width: 120}} />
          <button onClick={fetchChEMBL} disabled={chemblLoading} style={{marginLeft: 8}}>
            {chemblLoading ? 'Loading...' : 'Fetch'}
          </button>
          {chemblError && <div style={{color: 'red'}}>{chemblError}</div>}
          {chemblCompound && (
            <div style={{marginTop: 10, background: '#f4f4f4', padding: 12, borderRadius: 8, width: '100%', boxSizing: 'border-box', overflowX: 'auto'}}>
              <strong>ChEMBL ID:</strong> {chemblCompound.molecule_chembl_id}<br />
              <strong>Preferred Name:</strong> {chemblCompound.pref_name || 'N/A'}<br />
              <strong>Molecule Type:</strong> {chemblCompound.molecule_type}<br />
              <strong>Canonical SMILES:</strong> {chemblCompound.molecule_structures?.canonical_smiles || 'N/A'}<br />
              <pre style={{fontSize: 12, marginTop: 10, width: '100%', maxWidth: '100%', overflowX: 'auto', whiteSpace: 'pre', wordBreak: 'break-all'}}>{JSON.stringify(chemblCompound, null, 2)}</pre>
            </div>
          )}
        </div>
      </div>
      {analytics}
    </div>
  );
}

export default PublicApiDemo;
