from pylint.lint import Run

results = Run(['bvr/'], do_exit=False)

final_score = results.linter.stats['global_note']

if final_score < 8:
    raise Exception('Pylint Score Was Less Than 8: {}'.format(final_score))
exit(1)
