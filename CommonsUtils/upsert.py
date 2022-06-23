from delta.tables import *

def delta_table_upsert(table_name, updatesDF, tables_pk=[],when_matched={},not_matched = {}):

    """ Upserts new data from the DataFrame specified in 'UpdatesDF' into the delta table in 'table_path'.
    For more information, consult delta_table documentation at https://docs.delta.io/0.4.0/delta-update.html#upsert-into-a-table-using-merge

    Args:
        table_name (str): The name of the table that will be updated.
        tb_update_with (DataFrame): DataFrame containing the changes that will be upserted into the table.
        tables_pk (list(str)): List containing the primary_key columns that will be compared in order to merge.
        when_matched (dict(str)): Dictionary containing the clauses of update for when the values match.
        not_matched (dict(str)): Dictionary containing the clauses of update for when the values do not match
   """

    deltaTable = DeltaTable.forName(spark, table_name)

    if(when_matched == {} and not_matched=={}):
        deltaTable.alias("to_update").merge(
            updatesDF.alias("updates"),
            "to_update.{} = updates.{}".format(tables_pk[0],tables_pk[1])) \
          .whenMatchedUpdateAll() \
          .whenNotMatchedInsertAll() \
          .execute()
    elif(when_matched != {} and not_matched!={}):
        deltaTable.alias("to_update").merge(
            updatesDF.alias("updates"),
            "to_update.{} = updates.{}".format(tables_pk[0],tables_pk[1])) \
          .whenMatchedUpdate(set = when_matched ) \
          .whenNotMatchedInsert(values = not_matched) \
          .execute()
    elif(when_matched != {} and not_matched=={}):
        deltaTable.alias("to_update").merge(
            updatesDF.alias("updates"),
            "to_update.{} = updates.{}".format(tables_pk[0],tables_pk[1])) \
          .whenMatchedUpdate(set = when_matched ) \
          .whenNotMatchedInsertAll() \
          .execute()
    else:
        deltaTable.alias("to_update").merge(
            updatesDF.alias("updates"),
            "to_update.{} = updates.{}".format(tables_pk[0],tables_pk[1])) \
          .whenMatchedUpdateAll() \
          .whenNotMatchedInsert(values = not_matched) \
          .execute()