
import logging
import json

from Bio import SeqIO


log = logging.getLogger('io')


def import_contigs(contigs_path, min_length):
    """Apply min-length filters and rename contig headers."""

    contig_counter = 1
    contigs = []
    discarded = []
    with contigs_path.open() as fh:
        for record in SeqIO.parse(fh, 'fasta'):
            seq = str(record.seq)
            contig_name = "contig_%d" % contig_counter
            contig_counter += 1
            contig = {
                'id': contig_name,
                'org_id': record.id,
                'org_desc': record.description,
                'sequence': seq,
                'length': len(seq)
            }
            if len(seq) >= min_length:
                contigs.append(contig)
            else:
                discarded.append(contig)

    return contigs, discarded


def export_contigs(contigs, fasta_path):
    """Write valid contigs to Fasta file."""
    with fasta_path.open('w') as fh:
        for c in contigs:
            fh.write(">%s\n%s\n" % (c['id'], c['sequence']))


def write_json(annotations, json_path):
    """Export annotations as comprehensive JSON file."""
    with json_path.open('w') as fh:
        json.dump(annotations, fh, sort_keys=True, indent=4)
    return


def write_gff3(annotations, gff3_path):
    """Export annotations in GFF3 format."""
    return


def write_genbank(annotations, genbank_path):
    """Export annotations in GenBank format."""
    return


def write_embl(annotations, embl_path):
    """Export annotations in EMBL format."""
    return
