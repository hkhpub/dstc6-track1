
import numpy as np
import json


def do_parse_cmdline():

    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("--input_task_file", dest="inputtaskfile",
                      default="../data/dialog-task1API-kb1_atmosphere-distr0.5-trn10000.json",
                      # default="../data/dialog-task2REFINE-kb1_atmosphere-distr0.5-trn10000.json",
                      # default="../data/dialog-task3OPTIONS-kb1_atmosphere-distr0.5-trn10000.json",
                      # default="../data/dialog-task4INFOS-kb1_atmosphere-distr0.5-trn10000.json",
                      # default="../data/dialog-task5FULL-kb1_atmosphere-distr0.5-trn10000.json",
                      help="filename of the task", metavar="FILE")

    parser.add_option("--output_answer_file", dest="outputresultfile",
                      default="../output/output-task1-truth.json",
                      help="output file results", metavar="FILE")

    (options, args) = parser.parse_args()

    return options.inputtaskfile, options.outputresultfile

### The current dialog format
### [{dialog_id : " ", lst_candidate_id: [{candidate_id: " ", rank: " "}, ...]}]

if __name__ == '__main__':

    # Parsing command line
    inputtaskfile, outputanswerfile = do_parse_cmdline()

    fd = open(inputtaskfile, 'rb')
    json_data = json.load(fd)
    fd.close()

    lst_answers = []

    for idx_story, story in enumerate(json_data):
        dict_answer_current = {}
        dict_answer_current['dialog_id'] = story['dialog_id']
        dict_answer_current["lst_candidate_id"] = []
        answer_candidate = {
            "candidate_id": story['answer']['candidate_id'],
            "rank": 1,
        }
        dict_answer_current["lst_candidate_id"] += [answer_candidate]
        lst_answers += [dict_answer_current]

    fd = open(outputanswerfile, 'wb')
    json.dump(lst_answers, fd)
    fd.close()