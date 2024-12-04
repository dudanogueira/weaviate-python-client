# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/generative.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from weaviate.proto.v1 import base_pb2 as v1_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13v1/generative.proto\x12\x0bweaviate.v1\x1a\rv1/base.proto"\xce\x03\n\x10GenerativeSearch\x12"\n\x16single_response_prompt\x18\x01 \x01(\tB\x02\x18\x01\x12!\n\x15grouped_response_task\x18\x02 \x01(\tB\x02\x18\x01\x12\x1e\n\x12grouped_properties\x18\x03 \x03(\tB\x02\x18\x01\x12\x34\n\x06single\x18\x04 \x01(\x0b\x32$.weaviate.v1.GenerativeSearch.Single\x12\x36\n\x07grouped\x18\x05 \x01(\x0b\x32%.weaviate.v1.GenerativeSearch.Grouped\x1aY\n\x06Single\x12\x0e\n\x06prompt\x18\x01 \x01(\t\x12\r\n\x05\x64\x65\x62ug\x18\x02 \x01(\x08\x12\x30\n\x07queries\x18\x03 \x03(\x0b\x32\x1f.weaviate.v1.GenerativeProvider\x1a\x89\x01\n\x07Grouped\x12\x0c\n\x04task\x18\x01 \x01(\t\x12/\n\nproperties\x18\x02 \x01(\x0b\x32\x16.weaviate.v1.TextArrayH\x00\x88\x01\x01\x12\x30\n\x07queries\x18\x03 \x03(\x0b\x32\x1f.weaviate.v1.GenerativeProviderB\r\n\x0b_properties"\xe4\x04\n\x12GenerativeProvider\x12\x17\n\x0freturn_metadata\x18\x01 \x01(\x08\x12\x35\n\tanthropic\x18\x02 \x01(\x0b\x32 .weaviate.v1.GenerativeAnthropicH\x00\x12\x33\n\x08\x61nyscale\x18\x03 \x01(\x0b\x32\x1f.weaviate.v1.GenerativeAnyscaleH\x00\x12)\n\x03\x61ws\x18\x04 \x01(\x0b\x32\x1a.weaviate.v1.GenerativeAWSH\x00\x12/\n\x06\x63ohere\x18\x05 \x01(\x0b\x32\x1d.weaviate.v1.GenerativeCohereH\x00\x12-\n\x05\x64ummy\x18\x06 \x01(\x0b\x32\x1c.weaviate.v1.GenerativeDummyH\x00\x12\x31\n\x07mistral\x18\x07 \x01(\x0b\x32\x1e.weaviate.v1.GenerativeMistralH\x00\x12/\n\x06ollama\x18\x08 \x01(\x0b\x32\x1d.weaviate.v1.GenerativeOllamaH\x00\x12/\n\x06openai\x18\t \x01(\x0b\x32\x1d.weaviate.v1.GenerativeOpenAIH\x00\x12/\n\x06google\x18\n \x01(\x0b\x32\x1d.weaviate.v1.GenerativeGoogleH\x00\x12\x37\n\ndatabricks\x18\x0b \x01(\x0b\x32!.weaviate.v1.GenerativeDatabricksH\x00\x12\x37\n\nfriendliai\x18\x0c \x01(\x0b\x32!.weaviate.v1.GenerativeFriendliAIH\x00\x42\x06\n\x04kind"\xad\x02\n\x13GenerativeAnthropic\x12\x15\n\x08\x62\x61se_url\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nmax_tokens\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x12\n\x05model\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0btemperature\x18\x04 \x01(\x01H\x03\x88\x01\x01\x12\x12\n\x05top_k\x18\x05 \x01(\x03H\x04\x88\x01\x01\x12\x12\n\x05top_p\x18\x06 \x01(\x01H\x05\x88\x01\x01\x12\x33\n\x0estop_sequences\x18\x07 \x01(\x0b\x32\x16.weaviate.v1.TextArrayH\x06\x88\x01\x01\x42\x0b\n\t_base_urlB\r\n\x0b_max_tokensB\x08\n\x06_modelB\x0e\n\x0c_temperatureB\x08\n\x06_top_kB\x08\n\x06_top_pB\x11\n\x0f_stop_sequences"\x80\x01\n\x12GenerativeAnyscale\x12\x15\n\x08\x62\x61se_url\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05model\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0btemperature\x18\x03 \x01(\x01H\x02\x88\x01\x01\x42\x0b\n\t_base_urlB\x08\n\x06_modelB\x0e\n\x0c_temperature"\x99\x02\n\rGenerativeAWS\x12\x12\n\x05model\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0btemperature\x18\x08 \x01(\x01H\x01\x88\x01\x01\x12\x14\n\x07service\x18\t \x01(\tH\x02\x88\x01\x01\x12\x13\n\x06region\x18\n \x01(\tH\x03\x88\x01\x01\x12\x15\n\x08\x65ndpoint\x18\x0b \x01(\tH\x04\x88\x01\x01\x12\x19\n\x0ctarget_model\x18\x0c \x01(\tH\x05\x88\x01\x01\x12\x1b\n\x0etarget_variant\x18\r \x01(\tH\x06\x88\x01\x01\x42\x08\n\x06_modelB\x0e\n\x0c_temperatureB\n\n\x08_serviceB\t\n\x07_regionB\x0b\n\t_endpointB\x0f\n\r_target_modelB\x11\n\x0f_target_variant"\x84\x03\n\x10GenerativeCohere\x12\x15\n\x08\x62\x61se_url\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1e\n\x11\x66requency_penalty\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x17\n\nmax_tokens\x18\x03 \x01(\x03H\x02\x88\x01\x01\x12\x12\n\x05model\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x0e\n\x01k\x18\x05 \x01(\x03H\x04\x88\x01\x01\x12\x0e\n\x01p\x18\x06 \x01(\x01H\x05\x88\x01\x01\x12\x1d\n\x10presence_penalty\x18\x07 \x01(\x01H\x06\x88\x01\x01\x12\x33\n\x0estop_sequences\x18\x08 \x01(\x0b\x32\x16.weaviate.v1.TextArrayH\x07\x88\x01\x01\x12\x18\n\x0btemperature\x18\t \x01(\x01H\x08\x88\x01\x01\x42\x0b\n\t_base_urlB\x14\n\x12_frequency_penaltyB\r\n\x0b_max_tokensB\x08\n\x06_modelB\x04\n\x02_kB\x04\n\x02_pB\x13\n\x11_presence_penaltyB\x11\n\x0f_stop_sequencesB\x0e\n\x0c_temperature"\x11\n\x0fGenerativeDummy"\xc5\x01\n\x11GenerativeMistral\x12\x15\n\x08\x62\x61se_url\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nmax_tokens\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x12\n\x05model\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0btemperature\x18\x04 \x01(\x01H\x03\x88\x01\x01\x12\x12\n\x05top_p\x18\x05 \x01(\x01H\x04\x88\x01\x01\x42\x0b\n\t_base_urlB\r\n\x0b_max_tokensB\x08\n\x06_modelB\x0e\n\x0c_temperatureB\x08\n\x06_top_p"\x86\x01\n\x10GenerativeOllama\x12\x19\n\x0c\x61pi_endpoint\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05model\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0btemperature\x18\x03 \x01(\x01H\x02\x88\x01\x01\x42\x0f\n\r_api_endpointB\x08\n\x06_modelB\x0e\n\x0c_temperature"\x93\x04\n\x10GenerativeOpenAI\x12\x1e\n\x11\x66requency_penalty\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x17\n\nmax_tokens\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\r\n\x05model\x18\x03 \x01(\t\x12\x0e\n\x01n\x18\x04 \x01(\x03H\x02\x88\x01\x01\x12\x1d\n\x10presence_penalty\x18\x05 \x01(\x01H\x03\x88\x01\x01\x12)\n\x04stop\x18\x06 \x01(\x0b\x32\x16.weaviate.v1.TextArrayH\x04\x88\x01\x01\x12\x18\n\x0btemperature\x18\x07 \x01(\x01H\x05\x88\x01\x01\x12\x12\n\x05top_p\x18\x08 \x01(\x01H\x06\x88\x01\x01\x12\x15\n\x08\x62\x61se_url\x18\t \x01(\tH\x07\x88\x01\x01\x12\x18\n\x0b\x61pi_version\x18\n \x01(\tH\x08\x88\x01\x01\x12\x1a\n\rresource_name\x18\x0b \x01(\tH\t\x88\x01\x01\x12\x1a\n\rdeployment_id\x18\x0c \x01(\tH\n\x88\x01\x01\x12\x15\n\x08is_azure\x18\r \x01(\x08H\x0b\x88\x01\x01\x42\x14\n\x12_frequency_penaltyB\r\n\x0b_max_tokensB\x04\n\x02_nB\x13\n\x11_presence_penaltyB\x07\n\x05_stopB\x0e\n\x0c_temperatureB\x08\n\x06_top_pB\x0b\n\t_base_urlB\x0e\n\x0c_api_versionB\x10\n\x0e_resource_nameB\x10\n\x0e_deployment_idB\x0b\n\t_is_azure"\x8e\x04\n\x10GenerativeGoogle\x12\x1e\n\x11\x66requency_penalty\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x17\n\nmax_tokens\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x12\n\x05model\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1d\n\x10presence_penalty\x18\x04 \x01(\x01H\x03\x88\x01\x01\x12\x18\n\x0btemperature\x18\x05 \x01(\x01H\x04\x88\x01\x01\x12\x12\n\x05top_k\x18\x06 \x01(\x03H\x05\x88\x01\x01\x12\x12\n\x05top_p\x18\x07 \x01(\x01H\x06\x88\x01\x01\x12\x33\n\x0estop_sequences\x18\x08 \x01(\x0b\x32\x16.weaviate.v1.TextArrayH\x07\x88\x01\x01\x12\x19\n\x0c\x61pi_endpoint\x18\t \x01(\tH\x08\x88\x01\x01\x12\x17\n\nproject_id\x18\n \x01(\tH\t\x88\x01\x01\x12\x18\n\x0b\x65ndpoint_id\x18\x0b \x01(\tH\n\x88\x01\x01\x12\x13\n\x06region\x18\x0c \x01(\tH\x0b\x88\x01\x01\x42\x14\n\x12_frequency_penaltyB\r\n\x0b_max_tokensB\x08\n\x06_modelB\x13\n\x11_presence_penaltyB\x0e\n\x0c_temperatureB\x08\n\x06_top_kB\x08\n\x06_top_pB\x11\n\x0f_stop_sequencesB\x0f\n\r_api_endpointB\r\n\x0b_project_idB\x0e\n\x0c_endpoint_idB\t\n\x07_region"\xd0\x03\n\x14GenerativeDatabricks\x12\x15\n\x08\x65ndpoint\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05model\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x11\x66requency_penalty\x18\x03 \x01(\x01H\x02\x88\x01\x01\x12\x16\n\tlog_probs\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x1a\n\rtop_log_probs\x18\x05 \x01(\x03H\x04\x88\x01\x01\x12\x17\n\nmax_tokens\x18\x06 \x01(\x03H\x05\x88\x01\x01\x12\x0e\n\x01n\x18\x07 \x01(\x03H\x06\x88\x01\x01\x12\x1d\n\x10presence_penalty\x18\x08 \x01(\x01H\x07\x88\x01\x01\x12)\n\x04stop\x18\t \x01(\x0b\x32\x16.weaviate.v1.TextArrayH\x08\x88\x01\x01\x12\x18\n\x0btemperature\x18\n \x01(\x01H\t\x88\x01\x01\x12\x12\n\x05top_p\x18\x0b \x01(\x01H\n\x88\x01\x01\x42\x0b\n\t_endpointB\x08\n\x06_modelB\x14\n\x12_frequency_penaltyB\x0c\n\n_log_probsB\x10\n\x0e_top_log_probsB\r\n\x0b_max_tokensB\x04\n\x02_nB\x13\n\x11_presence_penaltyB\x07\n\x05_stopB\x0e\n\x0c_temperatureB\x08\n\x06_top_p"\xde\x01\n\x14GenerativeFriendliAI\x12\x15\n\x08\x62\x61se_url\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05model\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nmax_tokens\x18\x03 \x01(\x03H\x02\x88\x01\x01\x12\x18\n\x0btemperature\x18\x04 \x01(\x01H\x03\x88\x01\x01\x12\x0e\n\x01n\x18\x05 \x01(\x03H\x04\x88\x01\x01\x12\x12\n\x05top_p\x18\x06 \x01(\x01H\x05\x88\x01\x01\x42\x0b\n\t_base_urlB\x08\n\x06_modelB\r\n\x0b_max_tokensB\x0e\n\x0c_temperatureB\x04\n\x02_nB\x08\n\x06_top_p"\x92\x01\n\x1bGenerativeAnthropicMetadata\x12=\n\x05usage\x18\x01 \x01(\x0b\x32..weaviate.v1.GenerativeAnthropicMetadata.Usage\x1a\x34\n\x05Usage\x12\x14\n\x0cinput_tokens\x18\x01 \x01(\x03\x12\x15\n\routput_tokens\x18\x02 \x01(\x03"\x1c\n\x1aGenerativeAnyscaleMetadata"\x17\n\x15GenerativeAWSMetadata"\x9c\x06\n\x18GenerativeCohereMetadata\x12J\n\x0b\x61pi_version\x18\x01 \x01(\x0b\x32\x30.weaviate.v1.GenerativeCohereMetadata.ApiVersionH\x00\x88\x01\x01\x12L\n\x0c\x62illed_units\x18\x02 \x01(\x0b\x32\x31.weaviate.v1.GenerativeCohereMetadata.BilledUnitsH\x01\x88\x01\x01\x12\x41\n\x06tokens\x18\x03 \x01(\x0b\x32,.weaviate.v1.GenerativeCohereMetadata.TokensH\x02\x88\x01\x01\x12-\n\x08warnings\x18\x04 \x01(\x0b\x32\x16.weaviate.v1.TextArrayH\x03\x88\x01\x01\x1a\x8e\x01\n\nApiVersion\x12\x14\n\x07version\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\ris_deprecated\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x1c\n\x0fis_experimental\x18\x03 \x01(\x08H\x02\x88\x01\x01\x42\n\n\x08_versionB\x10\n\x0e_is_deprecatedB\x12\n\x10_is_experimental\x1a\xc5\x01\n\x0b\x42illedUnits\x12\x19\n\x0cinput_tokens\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x1a\n\routput_tokens\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x19\n\x0csearch_units\x18\x03 \x01(\x01H\x02\x88\x01\x01\x12\x1c\n\x0f\x63lassifications\x18\x04 \x01(\x01H\x03\x88\x01\x01\x42\x0f\n\r_input_tokensB\x10\n\x0e_output_tokensB\x0f\n\r_search_unitsB\x12\n\x10_classifications\x1a\x62\n\x06Tokens\x12\x19\n\x0cinput_tokens\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x1a\n\routput_tokens\x18\x02 \x01(\x01H\x01\x88\x01\x01\x42\x0f\n\r_input_tokensB\x10\n\x0e_output_tokensB\x0e\n\x0c_api_versionB\x0f\n\r_billed_unitsB\t\n\x07_tokensB\x0b\n\t_warnings"\x19\n\x17GenerativeDummyMetadata"\x81\x02\n\x19GenerativeMistralMetadata\x12@\n\x05usage\x18\x01 \x01(\x0b\x32,.weaviate.v1.GenerativeMistralMetadata.UsageH\x00\x88\x01\x01\x1a\x97\x01\n\x05Usage\x12\x1a\n\rprompt_tokens\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x1e\n\x11\x63ompletion_tokens\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x19\n\x0ctotal_tokens\x18\x03 \x01(\x03H\x02\x88\x01\x01\x42\x10\n\x0e_prompt_tokensB\x14\n\x12_completion_tokensB\x0f\n\r_total_tokensB\x08\n\x06_usage"\x1a\n\x18GenerativeOllamaMetadata"\xff\x01\n\x18GenerativeOpenAIMetadata\x12?\n\x05usage\x18\x01 \x01(\x0b\x32+.weaviate.v1.GenerativeOpenAIMetadata.UsageH\x00\x88\x01\x01\x1a\x97\x01\n\x05Usage\x12\x1a\n\rprompt_tokens\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x1e\n\x11\x63ompletion_tokens\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x19\n\x0ctotal_tokens\x18\x03 \x01(\x03H\x02\x88\x01\x01\x42\x10\n\x0e_prompt_tokensB\x14\n\x12_completion_tokensB\x0f\n\r_total_tokensB\x08\n\x06_usage"\xe8\x06\n\x18GenerativeGoogleMetadata\x12\x45\n\x08metadata\x18\x01 \x01(\x0b\x32..weaviate.v1.GenerativeGoogleMetadata.MetadataH\x00\x88\x01\x01\x12P\n\x0eusage_metadata\x18\x02 \x01(\x0b\x32\x33.weaviate.v1.GenerativeGoogleMetadata.UsageMetadataH\x01\x88\x01\x01\x1a~\n\nTokenCount\x12&\n\x19total_billable_characters\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x19\n\x0ctotal_tokens\x18\x02 \x01(\x03H\x01\x88\x01\x01\x42\x1c\n\x1a_total_billable_charactersB\x0f\n\r_total_tokens\x1a\xe1\x01\n\rTokenMetadata\x12P\n\x11input_token_count\x18\x01 \x01(\x0b\x32\x30.weaviate.v1.GenerativeGoogleMetadata.TokenCountH\x00\x88\x01\x01\x12Q\n\x12output_token_count\x18\x02 \x01(\x0b\x32\x30.weaviate.v1.GenerativeGoogleMetadata.TokenCountH\x01\x88\x01\x01\x42\x14\n\x12_input_token_countB\x15\n\x13_output_token_count\x1ao\n\x08Metadata\x12P\n\x0etoken_metadata\x18\x01 \x01(\x0b\x32\x33.weaviate.v1.GenerativeGoogleMetadata.TokenMetadataH\x00\x88\x01\x01\x42\x11\n\x0f_token_metadata\x1a\xbd\x01\n\rUsageMetadata\x12\x1f\n\x12prompt_token_count\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12#\n\x16\x63\x61ndidates_token_count\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x1e\n\x11total_token_count\x18\x03 \x01(\x03H\x02\x88\x01\x01\x42\x15\n\x13_prompt_token_countB\x19\n\x17_candidates_token_countB\x14\n\x12_total_token_countB\x0b\n\t_metadataB\x11\n\x0f_usage_metadata"\x87\x02\n\x1cGenerativeDatabricksMetadata\x12\x43\n\x05usage\x18\x01 \x01(\x0b\x32/.weaviate.v1.GenerativeDatabricksMetadata.UsageH\x00\x88\x01\x01\x1a\x97\x01\n\x05Usage\x12\x1a\n\rprompt_tokens\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x1e\n\x11\x63ompletion_tokens\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x19\n\x0ctotal_tokens\x18\x03 \x01(\x03H\x02\x88\x01\x01\x42\x10\n\x0e_prompt_tokensB\x14\n\x12_completion_tokensB\x0f\n\r_total_tokensB\x08\n\x06_usage"\x87\x02\n\x1cGenerativeFriendliAIMetadata\x12\x43\n\x05usage\x18\x01 \x01(\x0b\x32/.weaviate.v1.GenerativeFriendliAIMetadata.UsageH\x00\x88\x01\x01\x1a\x97\x01\n\x05Usage\x12\x1a\n\rprompt_tokens\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x1e\n\x11\x63ompletion_tokens\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x19\n\x0ctotal_tokens\x18\x03 \x01(\x03H\x02\x88\x01\x01\x42\x10\n\x0e_prompt_tokensB\x14\n\x12_completion_tokensB\x0f\n\r_total_tokensB\x08\n\x06_usage"\xa3\x05\n\x12GenerativeMetadata\x12=\n\tanthropic\x18\x01 \x01(\x0b\x32(.weaviate.v1.GenerativeAnthropicMetadataH\x00\x12;\n\x08\x61nyscale\x18\x02 \x01(\x0b\x32\'.weaviate.v1.GenerativeAnyscaleMetadataH\x00\x12\x31\n\x03\x61ws\x18\x03 \x01(\x0b\x32".weaviate.v1.GenerativeAWSMetadataH\x00\x12\x37\n\x06\x63ohere\x18\x04 \x01(\x0b\x32%.weaviate.v1.GenerativeCohereMetadataH\x00\x12\x35\n\x05\x64ummy\x18\x05 \x01(\x0b\x32$.weaviate.v1.GenerativeDummyMetadataH\x00\x12\x39\n\x07mistral\x18\x06 \x01(\x0b\x32&.weaviate.v1.GenerativeMistralMetadataH\x00\x12\x37\n\x06ollama\x18\x07 \x01(\x0b\x32%.weaviate.v1.GenerativeOllamaMetadataH\x00\x12\x37\n\x06openai\x18\x08 \x01(\x0b\x32%.weaviate.v1.GenerativeOpenAIMetadataH\x00\x12\x37\n\x06google\x18\t \x01(\x0b\x32%.weaviate.v1.GenerativeGoogleMetadataH\x00\x12?\n\ndatabricks\x18\n \x01(\x0b\x32).weaviate.v1.GenerativeDatabricksMetadataH\x00\x12?\n\nfriendliai\x18\x0b \x01(\x0b\x32).weaviate.v1.GenerativeFriendliAIMetadataH\x00\x42\x06\n\x04kind"\xa2\x01\n\x0fGenerativeReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x30\n\x05\x64\x65\x62ug\x18\x02 \x01(\x0b\x32\x1c.weaviate.v1.GenerativeDebugH\x00\x88\x01\x01\x12\x36\n\x08metadata\x18\x03 \x01(\x0b\x32\x1f.weaviate.v1.GenerativeMetadataH\x01\x88\x01\x01\x42\x08\n\x06_debugB\x0b\n\t_metadata"@\n\x10GenerativeResult\x12,\n\x06values\x18\x01 \x03(\x0b\x32\x1c.weaviate.v1.GenerativeReply";\n\x0fGenerativeDebug\x12\x18\n\x0b\x66ull_prompt\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_full_promptBt\n#io.weaviate.client.grpc.protocol.v1B\x17WeaviateProtoGenerativeZ4github.com/weaviate/weaviate/grpc/generated;protocolb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.generative_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"\n#io.weaviate.client.grpc.protocol.v1B\027WeaviateProtoGenerativeZ4github.com/weaviate/weaviate/grpc/generated;protocol"
    )
    _globals["_GENERATIVESEARCH"].fields_by_name["single_response_prompt"]._options = None
    _globals["_GENERATIVESEARCH"].fields_by_name[
        "single_response_prompt"
    ]._serialized_options = b"\030\001"
    _globals["_GENERATIVESEARCH"].fields_by_name["grouped_response_task"]._options = None
    _globals["_GENERATIVESEARCH"].fields_by_name[
        "grouped_response_task"
    ]._serialized_options = b"\030\001"
    _globals["_GENERATIVESEARCH"].fields_by_name["grouped_properties"]._options = None
    _globals["_GENERATIVESEARCH"].fields_by_name[
        "grouped_properties"
    ]._serialized_options = b"\030\001"
    _globals["_GENERATIVESEARCH"]._serialized_start = 52
    _globals["_GENERATIVESEARCH"]._serialized_end = 514
    _globals["_GENERATIVESEARCH_SINGLE"]._serialized_start = 285
    _globals["_GENERATIVESEARCH_SINGLE"]._serialized_end = 374
    _globals["_GENERATIVESEARCH_GROUPED"]._serialized_start = 377
    _globals["_GENERATIVESEARCH_GROUPED"]._serialized_end = 514
    _globals["_GENERATIVEPROVIDER"]._serialized_start = 517
    _globals["_GENERATIVEPROVIDER"]._serialized_end = 1129
    _globals["_GENERATIVEANTHROPIC"]._serialized_start = 1132
    _globals["_GENERATIVEANTHROPIC"]._serialized_end = 1433
    _globals["_GENERATIVEANYSCALE"]._serialized_start = 1436
    _globals["_GENERATIVEANYSCALE"]._serialized_end = 1564
    _globals["_GENERATIVEAWS"]._serialized_start = 1567
    _globals["_GENERATIVEAWS"]._serialized_end = 1848
    _globals["_GENERATIVECOHERE"]._serialized_start = 1851
    _globals["_GENERATIVECOHERE"]._serialized_end = 2239
    _globals["_GENERATIVEDUMMY"]._serialized_start = 2241
    _globals["_GENERATIVEDUMMY"]._serialized_end = 2258
    _globals["_GENERATIVEMISTRAL"]._serialized_start = 2261
    _globals["_GENERATIVEMISTRAL"]._serialized_end = 2458
    _globals["_GENERATIVEOLLAMA"]._serialized_start = 2461
    _globals["_GENERATIVEOLLAMA"]._serialized_end = 2595
    _globals["_GENERATIVEOPENAI"]._serialized_start = 2598
    _globals["_GENERATIVEOPENAI"]._serialized_end = 3129
    _globals["_GENERATIVEGOOGLE"]._serialized_start = 3132
    _globals["_GENERATIVEGOOGLE"]._serialized_end = 3658
    _globals["_GENERATIVEDATABRICKS"]._serialized_start = 3661
    _globals["_GENERATIVEDATABRICKS"]._serialized_end = 4125
    _globals["_GENERATIVEFRIENDLIAI"]._serialized_start = 4128
    _globals["_GENERATIVEFRIENDLIAI"]._serialized_end = 4350
    _globals["_GENERATIVEANTHROPICMETADATA"]._serialized_start = 4353
    _globals["_GENERATIVEANTHROPICMETADATA"]._serialized_end = 4499
    _globals["_GENERATIVEANTHROPICMETADATA_USAGE"]._serialized_start = 4447
    _globals["_GENERATIVEANTHROPICMETADATA_USAGE"]._serialized_end = 4499
    _globals["_GENERATIVEANYSCALEMETADATA"]._serialized_start = 4501
    _globals["_GENERATIVEANYSCALEMETADATA"]._serialized_end = 4529
    _globals["_GENERATIVEAWSMETADATA"]._serialized_start = 4531
    _globals["_GENERATIVEAWSMETADATA"]._serialized_end = 4554
    _globals["_GENERATIVECOHEREMETADATA"]._serialized_start = 4557
    _globals["_GENERATIVECOHEREMETADATA"]._serialized_end = 5353
    _globals["_GENERATIVECOHEREMETADATA_APIVERSION"]._serialized_start = 4854
    _globals["_GENERATIVECOHEREMETADATA_APIVERSION"]._serialized_end = 4996
    _globals["_GENERATIVECOHEREMETADATA_BILLEDUNITS"]._serialized_start = 4999
    _globals["_GENERATIVECOHEREMETADATA_BILLEDUNITS"]._serialized_end = 5196
    _globals["_GENERATIVECOHEREMETADATA_TOKENS"]._serialized_start = 5198
    _globals["_GENERATIVECOHEREMETADATA_TOKENS"]._serialized_end = 5296
    _globals["_GENERATIVEDUMMYMETADATA"]._serialized_start = 5355
    _globals["_GENERATIVEDUMMYMETADATA"]._serialized_end = 5380
    _globals["_GENERATIVEMISTRALMETADATA"]._serialized_start = 5383
    _globals["_GENERATIVEMISTRALMETADATA"]._serialized_end = 5640
    _globals["_GENERATIVEMISTRALMETADATA_USAGE"]._serialized_start = 5479
    _globals["_GENERATIVEMISTRALMETADATA_USAGE"]._serialized_end = 5630
    _globals["_GENERATIVEOLLAMAMETADATA"]._serialized_start = 5642
    _globals["_GENERATIVEOLLAMAMETADATA"]._serialized_end = 5668
    _globals["_GENERATIVEOPENAIMETADATA"]._serialized_start = 5671
    _globals["_GENERATIVEOPENAIMETADATA"]._serialized_end = 5926
    _globals["_GENERATIVEOPENAIMETADATA_USAGE"]._serialized_start = 5479
    _globals["_GENERATIVEOPENAIMETADATA_USAGE"]._serialized_end = 5630
    _globals["_GENERATIVEGOOGLEMETADATA"]._serialized_start = 5929
    _globals["_GENERATIVEGOOGLEMETADATA"]._serialized_end = 6801
    _globals["_GENERATIVEGOOGLEMETADATA_TOKENCOUNT"]._serialized_start = 6110
    _globals["_GENERATIVEGOOGLEMETADATA_TOKENCOUNT"]._serialized_end = 6236
    _globals["_GENERATIVEGOOGLEMETADATA_TOKENMETADATA"]._serialized_start = 6239
    _globals["_GENERATIVEGOOGLEMETADATA_TOKENMETADATA"]._serialized_end = 6464
    _globals["_GENERATIVEGOOGLEMETADATA_METADATA"]._serialized_start = 6466
    _globals["_GENERATIVEGOOGLEMETADATA_METADATA"]._serialized_end = 6577
    _globals["_GENERATIVEGOOGLEMETADATA_USAGEMETADATA"]._serialized_start = 6580
    _globals["_GENERATIVEGOOGLEMETADATA_USAGEMETADATA"]._serialized_end = 6769
    _globals["_GENERATIVEDATABRICKSMETADATA"]._serialized_start = 6804
    _globals["_GENERATIVEDATABRICKSMETADATA"]._serialized_end = 7067
    _globals["_GENERATIVEDATABRICKSMETADATA_USAGE"]._serialized_start = 5479
    _globals["_GENERATIVEDATABRICKSMETADATA_USAGE"]._serialized_end = 5630
    _globals["_GENERATIVEFRIENDLIAIMETADATA"]._serialized_start = 7070
    _globals["_GENERATIVEFRIENDLIAIMETADATA"]._serialized_end = 7333
    _globals["_GENERATIVEFRIENDLIAIMETADATA_USAGE"]._serialized_start = 5479
    _globals["_GENERATIVEFRIENDLIAIMETADATA_USAGE"]._serialized_end = 5630
    _globals["_GENERATIVEMETADATA"]._serialized_start = 7336
    _globals["_GENERATIVEMETADATA"]._serialized_end = 8011
    _globals["_GENERATIVEREPLY"]._serialized_start = 8014
    _globals["_GENERATIVEREPLY"]._serialized_end = 8176
    _globals["_GENERATIVERESULT"]._serialized_start = 8178
    _globals["_GENERATIVERESULT"]._serialized_end = 8242
    _globals["_GENERATIVEDEBUG"]._serialized_start = 8244
    _globals["_GENERATIVEDEBUG"]._serialized_end = 8303
# @@protoc_insertion_point(module_scope)
