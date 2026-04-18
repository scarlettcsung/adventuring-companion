from core.models.counter import ResetType


def perform_reset(features, rest_type):
    for f in [f for f in features if f.counter]:

        if rest_type == ResetType.DAILY and f.tracker.reset_type == ResetType.DAILY:
            f.tracker.reset()

        elif rest_type == ResetType.LONG and f.tracker.reset_type != ResetType.NONE:
            f.tracker.reset()

        elif rest_type == ResetType.SHORT and f.tracker.reset_type == ResetType.SHORT:
            f.tracker.reset()

    # TODO: Add spell slot reset logic when spell slots are done

def calculate_max_count(character,feature):
    counter_type = feature.counter.max_type
