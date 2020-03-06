#!/usr/bin/env python
#-------------------------------------------------------------------------
# extend_standalone_features.py
# add extra features for standalone mode
#-------------------------------------------------------------------------
import argparse
import traceback
import logging
import multiprocessing
import os
import gzip

import pysam
import numpy as np

import sequencing_features
import genomic_file_handlers as genome


def extract_features(candidate_record):
    work, reference, tumor_bam, normal_bam, chrom, pos, ref, alt, min_mapq, min_bq, dbsnp, cosmic = candidate_record
    thread_logger = logging.getLogger(
        "{} ({})".format(extend_standalone_features.__name__, multiprocessing.current_process().name))
    try:
        thread_logger.info(
            "---------------------Filter Candidates---------------------")
        tbam = pysam.AlignmentFile(tumor_bam)
        nbam = pysam.AlignmentFile(normal_bam)
        ref_fa = pysam.FastaFile(reference)

        my_coordinate = [chrom, int(pos)]
        nBamFeatures = sequencing_features.from_bam(
            nbam, my_coordinate, ref, alt, min_mapq, min_bq)
        tBamFeatures = sequencing_features.from_bam(
            tbam, my_coordinate, ref, alt, min_mapq, min_bq)

        n_ref = nBamFeatures['ref_for'] + nBamFeatures['ref_rev']
        n_alt = nBamFeatures['alt_for'] + nBamFeatures['alt_rev']
        t_ref = tBamFeatures['ref_for'] + tBamFeatures['ref_rev']
        t_alt = tBamFeatures['alt_for'] + tBamFeatures['alt_rev']
        sor = sequencing_features.somaticOddRatio(n_ref, n_alt, t_ref, t_alt)

        homopolymer_length, site_homopolymer_length = sequencing_features.from_genome_reference(
            ref_fa, my_coordinate, ref, alt)

        indel_length = len(alt) - len(ref)

        CHROM = my_coordinate[0]
        POS = my_coordinate[1]
        REF = ref_base
        ALT = first_alt
        if_dbsnp = if_dbsnp
        COMMON = if_common
        if_COSMIC = if_cosmic
        COSMIC_CNT = num_cases
        Consistent_Mates = tBamFeatures['consistent_mates']
        Inconsistent_Mates = tBamFeatures['inconsistent_mates']
        N_DP = nBamFeatures['dp']
        nBAM_REF_MQ = '%g' % nBamFeatures['ref_mq']
        nBAM_ALT_MQ = '%g' % nBamFeatures['alt_mq']
        nBAM_Z_Ranksums_MQ = '%g' % nBamFeatures['z_ranksums_mq']
        nBAM_REF_BQ = '%g' % nBamFeatures['ref_bq']
        nBAM_ALT_BQ = '%g' % nBamFeatures['alt_bq']
        nBAM_Z_Ranksums_BQ = '%g' % nBamFeatures['z_ranksums_bq']
        nBAM_REF_NM = '%g' % nBamFeatures['ref_NM']
        nBAM_ALT_NM = '%g' % nBamFeatures['alt_NM']
        nBAM_NM_Diff = '%g' % nBamFeatures['NM_Diff']
        nBAM_REF_Concordant = nBamFeatures['ref_concordant_reads']
        nBAM_REF_Discordant = nBamFeatures['ref_discordant_reads']
        nBAM_ALT_Concordant = nBamFeatures['alt_concordant_reads']
        nBAM_ALT_Discordant = nBamFeatures['alt_discordant_reads']
        nBAM_Concordance_FET = rescale(
            nBamFeatures['concordance_fet'], 'fraction', p_scale, 1001)
        N_REF_FOR = nBamFeatures['ref_for']
        N_REF_REV = nBamFeatures['ref_rev']
        N_ALT_FOR = nBamFeatures['alt_for']
        N_ALT_REV = nBamFeatures['alt_rev']
        nBAM_StrandBias_FET = rescale(
            nBamFeatures['strandbias_fet'], 'fraction', p_scale, 1001)
        nBAM_Z_Ranksums_EndPos = '%g' % nBamFeatures['z_ranksums_endpos']
        nBAM_REF_Clipped_Reads = nBamFeatures['ref_SC_reads']
        nBAM_ALT_Clipped_Reads = nBamFeatures['alt_SC_reads']
        nBAM_Clipping_FET = rescale(
            nBamFeatures['clipping_fet'], 'fraction', p_scale, 1001)
        nBAM_MQ0 = nBamFeatures['MQ0']
        nBAM_Other_Reads = nBamFeatures['noise_read_count']
        nBAM_Poor_Reads = nBamFeatures['poor_read_count']
        nBAM_REF_InDel_3bp = nBamFeatures['ref_indel_3bp']
        nBAM_REF_InDel_2bp = nBamFeatures['ref_indel_2bp']
        nBAM_REF_InDel_1bp = nBamFeatures['ref_indel_1bp']
        nBAM_ALT_InDel_3bp = nBamFeatures['alt_indel_3bp']
        nBAM_ALT_InDel_2bp = nBamFeatures['alt_indel_2bp']
        nBAM_ALT_InDel_1bp = nBamFeatures['alt_indel_1bp']
        SOR = sor
        MaxHomopolymer_Length = homopolymer_length
        SiteHomopolymer_Length = site_homopolymer_length
        T_DP = tBamFeatures['dp']
        tBAM_REF_MQ = '%g' % tBamFeatures['ref_mq']
        tBAM_ALT_MQ = '%g' % tBamFeatures['alt_mq']
        tBAM_Z_Ranksums_MQ = '%g' % tBamFeatures['z_ranksums_mq']
        tBAM_REF_BQ = '%g' % tBamFeatures['ref_bq']
        tBAM_ALT_BQ = '%g' % tBamFeatures['alt_bq']
        tBAM_Z_Ranksums_BQ = '%g' % tBamFeatures['z_ranksums_bq']
        tBAM_REF_NM = '%g' % tBamFeatures['ref_NM']
        tBAM_ALT_NM = '%g' % tBamFeatures['alt_NM']
        tBAM_NM_Diff = '%g' % tBamFeatures['NM_Diff']
        tBAM_REF_Concordant = tBamFeatures['ref_concordant_reads']
        tBAM_REF_Discordant = tBamFeatures['ref_discordant_reads']
        tBAM_ALT_Concordant = tBamFeatures['alt_concordant_reads']
        tBAM_ALT_Discordant = tBamFeatures['alt_discordant_reads']
        tBAM_Concordance_FET = rescale(
            tBamFeatures['concordance_fet'], 'fraction', p_scale, 1001)
        T_REF_FOR = tBamFeatures['ref_for']
        T_REF_REV = tBamFeatures['ref_rev']
        T_ALT_FOR = tBamFeatures['alt_for']
        T_ALT_REV = tBamFeatures['alt_rev']
        tBAM_StrandBias_FET = rescale(
            tBamFeatures['strandbias_fet'], 'fraction', p_scale, 1001)
        tBAM_Z_Ranksums_EndPos = '%g' % tBamFeatures['z_ranksums_endpos']
        tBAM_REF_Clipped_Reads = tBamFeatures['ref_SC_reads']
        tBAM_ALT_Clipped_Reads = tBamFeatures['alt_SC_reads']
        tBAM_Clipping_FET = rescale(
            tBamFeatures['clipping_fet'], 'fraction', p_scale, 1001)
        tBAM_MQ0 = tBamFeatures['MQ0']
        tBAM_Other_Reads = tBamFeatures['noise_read_count']
        tBAM_Poor_Reads = tBamFeatures['poor_read_count']
        tBAM_REF_InDel_3bp = tBamFeatures['ref_indel_3bp']
        tBAM_REF_InDel_2bp = tBamFeatures['ref_indel_2bp']
        tBAM_REF_InDel_1bp = tBamFeatures['ref_indel_1bp']
        tBAM_ALT_InDel_3bp = tBamFeatures['alt_indel_3bp']
        tBAM_ALT_InDel_2bp = tBamFeatures['alt_indel_2bp']
        tBAM_ALT_InDel_1bp = tBamFeatures['alt_indel_1bp']
        InDel_Length = indel_length

        # thread_logger.info(tBamFeatures)
        # aaa

        return 0

    except Exception as ex:
        thread_logger.error(traceback.format_exc())
        thread_logger.error(ex)
        return None


def extend_standalone_features(candidates_vcf,
                               reference, tumor_bam, normal_bam,
                               min_mapq, min_bq,
                               dbsnp, cosmic,
                               num_threads,
                               work):

    logger = logging.getLogger(extend_standalone_features.__name__)

    logger.info("----------------------Preprocessing------------------------")
    if not os.path.exists(work):
        os.mkdir(work)

    if not os.path.exists(tumor_bam):
        logger.error("Aborting!")
        raise Exception("No tumor BAM file {}".format(tumor_bam))
    if not os.path.exists(normal_bam):
        logger.error("Aborting!")
        raise Exception("No normal BAM file {}".format(normal_bam))
    if not os.path.exists(tumor_bam + ".bai"):
        logger.error("Aborting!")
        raise Exception(
            "No tumor .bai index file {}".format(tumor_bam + ".bai"))
    if not os.path.exists(normal_bam + ".bai"):
        logger.error("Aborting!")
        raise Exception(
            "No normal .bai index file {}".format(normal_bam + ".bai"))

    if dbsnp:
        with gzip.open(dbsnp,'rt') as i_f:
            for line in i_f:
                if not line.strip():
                    continue
                if line[0] == "#":
                    continue
                print(line)
                aaa
    pool = multiprocessing.Pool(num_threads)
    map_args = []
    with open(candidates_vcf) as i_f:
        for line in i_f:
            if not line.strip():
                continue
            if line[0] == "#":
                continue
            chrom, pos, _, ref, alt = line.strip().split("\t")[0:5]
            map_args.append((work, reference, tumor_bam, normal_bam,
                             chrom, pos, ref, alt, min_mapq, min_bq, dbsnp, cosmic))
    try:
        ext_features = pool.map_async(extract_features, map_args).get()
        pool.close()
    except Exception as inst:
        logger.error(inst)
        pool.close()
        traceback.print_exc()
        raise Exception


if __name__ == '__main__':
    FORMAT = '%(levelname)s %(asctime)-15s %(name)-20s %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(
        description='extract extra features for standalone mode')
    parser.add_argument('--candidates_vcf', type=str, help='candidates vcf',
                        required=True)
    parser.add_argument('--reference', type=str, help='reference fasta filename',
                        required=True)
    parser.add_argument('--tumor_bam', type=str,
                        help='tumor bam', required=True)
    parser.add_argument('--normal_bam', type=str,
                        help='normal bam', required=True)
    parser.add_argument('--min_mapq', type=int,
                        help='minimum mapping quality', default=1)
    parser.add_argument('--min_bq', type=float,
                        help='minimum base quality', default=5)
    parser.add_argument('--dbsnp', type=str,
                        help='dbSNP vcf (to annotate candidate variants)', default=None)
    parser.add_argument('--cosmic', type=str,
                        help='COSMIC vcf (to annotate candidate variants)', default=None)
    parser.add_argument('--num_threads', type=int,
                        help='number of threads', default=1)
    parser.add_argument('--work', type=str,
                        help='work directory', required=True)
    args = parser.parse_args()
    logger.info(args)

    try:
        output = extend_standalone_features(args.candidates_vcf,
                                            args.reference, args.tumor_bam, args.normal_bam,
                                            args.min_mapq, args.min_bq,
                                            args.dbsnp, args.cosmic,
                                            args.num_threads,
                                            args.work)
        if output is None:
            raise Exception("extend_standalone_features failed!")
    except Exception as e:
        logger.error(traceback.format_exc())
        logger.error("Aborting!")
        logger.error(
            "extend_standalone_features.py failure on arguments: {}".format(args))
        raise e