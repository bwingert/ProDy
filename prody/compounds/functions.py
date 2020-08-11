"""This module defines functions for using compounds from the PDB and elsewhere."""

from .pdbligands import PDBLigandRecord

__all__ = ['calc2DSimilarity']


def calc2DSimilarity(smiles1, smiles2):
    """Calculate 2D similarity using Morgan Fingerprints
    
    :arg smiles1: first SMILES string or PDBLigandRecord containing one
    :type smiles1: str, :class:`.PDBLigandRecord`

    :arg smiles2: second SMILES string or PDBLigandRecord containing one
    :type smiles2: str, :class:`.PDBLigandRecord`
    """
    try:
        from rdkit import Chem
        from rdkit import DataStructs
        from rdkit.Chem.Fingerprints import FingerprintMols
        from rdkit.Chem import AllChem
    except ImportError:
        raise ImportError('rdkit is a required package for calc2DSimilarity')

    if not isinstance(smiles1, str):
        try:
            smiles1 = smiles1.getCanonicalSMILES()
        except:
            raise TypeError('smiles1 should be a string or PDBLigandRecord')

    if not isinstance(smiles2, str):
        try:
            smiles2 = smiles2.getCanonicalSMILES()
        except:
            raise TypeError('smiles2 should be a string or PDBLigandRecord')

    m1 = Chem.MolFromSmiles(smiles1)
    m2 = Chem.MolFromSmiles(smiles2)
    if m1 is not None and m2 is not None:
        fp1 = AllChem.GetMorganFingerprint(m1, 2, useFeatures=True)
        fp2 = AllChem.GetMorganFingerprint(m2, 2, useFeatures=True)
        simi_score = DataStructs.TanimotoSimilarity(fp1, fp2)

    return simi_score