import { useState } from 'react';

// material-ui
import { OutlinedInput } from '@mui/material';

// third-party
import { Row, useAsyncDebounce } from 'react-table';

// assets
import SearchOutlined from '@ant-design/icons/SearchOutlined';

export function GlobalFilter({ preGlobalFilteredRows, globalFilter, setGlobalFilter, setters, ...other }: any) {
  const [localGlobalFilter, setLocalGlobalFilter] = useState<string>(globalFilter);

  const count =
    setters && setters.totalNumberOfLogs !== undefined && setters.totalNumberOfLogs !== null
      ? setters.totalNumberOfLogs
      : preGlobalFilteredRows.length;
  //console.log('current global after useState', JSON.stringify(localGlobalFilter));
  const onChange = useAsyncDebounce((value: any) => {
    setGlobalFilter(value);

    // odd way to override
    if (value === '') {
      setGlobalFilter(' ');
    }

    if (setters && setters.setPageNumber) {
      setters.setPageNumber(0);
    }
  }, 200);

  return (
    <>
      {/* <p>
        Value: {JSON.stringify(localGlobalFilter)} {localGlobalFilter === undefined ? 'undefined' : 'not undefined'}
      </p>
      <p>
        Global Value: {JSON.stringify(globalFilter)} {globalFilter === undefined ? 'undefined' : 'not undefined'}
      </p> */}
      <OutlinedInput
        value={localGlobalFilter !== null && localGlobalFilter !== undefined ? localGlobalFilter : ''}
        onChange={(e) => {
          setLocalGlobalFilter(e.target.value);
          onChange(e.target.value);
        }}
        placeholder={`Search ${count} records...`}
        id="start-adornment-email"
        startAdornment={<SearchOutlined />}
        {...other}
      />
    </>
  );
}

// @ts-ignore
function fuzzyTextFilterFn(rows, id, filterValue) {
  // @ts-ignore
  return matchSorter(rows, filterValue, { keys: [(row: any) => row.values[id]] });
}

fuzzyTextFilterFn.autoRemove = (val: any) => !val;

export const renderFilterTypes = () => ({
  fuzzyText: fuzzyTextFilterFn,
  text: (rows: Row[], id: string, filterValue: string) => {
    rows.filter((row: Row) => {
      const rowValue = row.values[id];
      return rowValue !== undefined ? String(rowValue).toLowerCase().startsWith(String(filterValue).toLowerCase()) : true;
    });
  }
});
