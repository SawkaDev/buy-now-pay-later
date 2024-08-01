import { useEffect, useMemo, Fragment } from 'react';
import { alpha, useTheme } from '@mui/material/styles';
import { Button, Stack, Table, TableBody, TableCell, TableHead, TableRow, useMediaQuery } from '@mui/material';
import { useExpanded, useGlobalFilter, useRowSelect, useSortBy, useTable, usePagination, useFilters, Column } from 'react-table';
import { GlobalFilter, renderFilterTypes } from './react-table';
import PlusOutlined from '@ant-design/icons/PlusOutlined';
import { HeaderSort, SortingSelect, TablePagination } from './table-components';

// ==============================|| REACT TABLE ||============================== //

export interface TableSetters {
  setPageNumber: (value: React.SetStateAction<number>) => void;
  setPageSize: (value: React.SetStateAction<number>) => void;
  setFilter: (value: React.SetStateAction<string>) => void;
  setSort: (value: React.SetStateAction<string>) => void;
  setColumnFilter: (value: React.SetStateAction<string>) => void;
  totalNumberOfLogs: number;
  pageNumber: number;
}

interface ReactTableProps {
  columns: Column[];
  data: [];
  getHeaderProps: (column: any) => void;
  handleAdd?: () => void;
  subComponent?: any;
  addButtonText?: string;
  filterWord?: string | null;
  setters?: TableSetters;
  customSortBy?: string;
  tableSize?: 'small' | 'medium';
}

export function ReactTable({
  columns,
  data,
  getHeaderProps,
  handleAdd,
  subComponent,
  addButtonText,
  filterWord,
  setters,
  customSortBy,
  tableSize = 'small'
}: ReactTableProps) {
  const theme = useTheme();
  const matchDownSM = useMediaQuery(theme.breakpoints.down('sm'));
  const filterTypes = useMemo(() => renderFilterTypes, []);
  var sortBy = { id: 'created_at', desc: true };

  if (customSortBy) {
    sortBy = { id: customSortBy, desc: true };
  }

  var initialState = {
    // @ts-ignore
    pageIndex: 0,
    // @ts-ignore
    pageSize: 10,
    // @ts-ignore
    hiddenColumns: ['age', 'test', 'patientId', 'diff', 'apiURL', 'nameSuffix']
  };

  // @ts-ignore
  initialState.sortBy = [sortBy];
  // if (setters) {
  //   // @ts-ignore
  //   initialState.sortBy = [sortBy];
  // }

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    prepareRow,
    setHiddenColumns,
    visibleColumns,
    allColumns,
    rows,
    // @ts-ignore
    page,
    // @ts-ignore
    gotoPage,
    // @ts-ignore
    setPageSize,
    // @ts-ignore
    state: { globalFilter, pageIndex, pageSize },
    // @ts-ignore
    preGlobalFilteredRows,
    // @ts-ignore
    setGlobalFilter,
    // @ts-ignore
    setSortBy,
    // @ts-ignore
    setFilter
  } = useTable(
    {
      columns,
      data,
      // @ts-ignore
      filterTypes,
      // @ts-ignore
      initialState: initialState,
      manualSortBy: setters ? true : false // may not need?
    },
    useFilters,
    useGlobalFilter,
    useSortBy,
    useExpanded,
    usePagination,
    useRowSelect
  );

  useEffect(() => {
    if (setters && setters.setFilter && globalFilter !== undefined) {
      // strange work around but it works
      if (globalFilter === ' ') {
        setters.setFilter('');
      }
      setters.setFilter(globalFilter);
    } else {
      // mainly for tests page since setters does not exist
      if (globalFilter !== undefined) {
        if (globalFilter === ' ') {
          setGlobalFilter('');
        } else {
          setGlobalFilter(globalFilter);
        }
      }
    }
  }, [globalFilter, filterWord]);

  useEffect(() => {
    if (setters && setters.setPageSize) {
      setters.setPageSize(pageSize);
    }
  }, [pageSize]);

  useEffect(() => {
    if (matchDownSM) {
      setHiddenColumns(['gender', 'updatedAt', 'age', 'test', 'patientId', 'diff', 'apiURL', 'nameSuffix']);
    } else {
      setHiddenColumns(['age', 'test', 'patientId', 'diff', 'apiURL', 'nameSuffix']);
    }
    // eslint-disable-next-line
  }, [matchDownSM]);

  return (
    <>
      <Stack spacing={3}>
        <Stack
          direction={matchDownSM ? 'column' : 'row'}
          spacing={1}
          justifyContent="space-between"
          alignItems="center"
          sx={{ p: 3, pb: 0 }}
        >
          <GlobalFilter
            preGlobalFilteredRows={preGlobalFilteredRows}
            globalFilter={globalFilter}
            setGlobalFilter={setGlobalFilter}
            size="small"
            setters={setters ? setters : null}
          />
          <Stack direction={matchDownSM ? 'column' : 'row'} alignItems="center" spacing={1}>
            <SortingSelect
              sortBy={sortBy.id}
              setSortBy={setSortBy}
              allColumns={allColumns}
              sortByCustom={setters && setters.setSort ? setters.setSort : null}
            />

            {handleAdd && (
              <Button variant="contained" startIcon={<PlusOutlined />} onClick={handleAdd}>
                {addButtonText}
              </Button>
            )}
          </Stack>
        </Stack>
        <Table {...getTableProps()} size={tableSize}>
          <TableHead>
            {headerGroups.map((headerGroup: any, i: number) => (
              <TableRow key={i} {...headerGroup.getHeaderGroupProps()}>
                {headerGroup.headers.map((column: any, index: number) => (
                  <TableCell key={index} {...column.getHeaderProps([{ className: column.className }, getHeaderProps(column)])}>
                    <HeaderSort column={column} setters={setters ? setters : null} />
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableHead>
          <TableBody {...getTableBodyProps()}>
            {page.map((row: any, i: number) => {
              prepareRow(row);
              const rowProps = row.getRowProps();

              return (
                <Fragment key={i}>
                  <TableRow
                    {...row.getRowProps()}
                    onDoubleClick={() => {
                      //   router.push();
                    }}
                    sx={{
                      bgcolor: row.isSelected ? alpha(theme.palette.primary.lighter, 0.35) : 'inherit',
                      '&:hover': { cursor: 'pointer' }
                    }}
                  >
                    {row.cells.map((cell: any, index: number) => (
                      <TableCell key={index} {...cell.getCellProps([{ className: cell.column.className }])}>
                        {cell.render('Cell')}
                      </TableCell>
                    ))}
                  </TableRow>
                  {row.isExpanded && subComponent({ row, rowProps, visibleColumns })}
                </Fragment>
              );
            })}

            {rows.length === 0 && (
              <TableRow>
                <TableCell align="center" colSpan={allColumns.length}>
                  No Data
                </TableCell>
              </TableRow>
            )}
            <TableRow sx={{ '&:hover': { bgcolor: 'transparent !important' } }}>
              <TableCell sx={{ p: 2, py: 3 }} colSpan={9}>
                <TablePagination
                  gotoPage={gotoPage}
                  rows={rows}
                  setPageSize={setPageSize}
                  pageSize={pageSize}
                  pageIndex={setters && setters.pageNumber ? setters.pageNumber : pageIndex}
                  setters={setters}
                />
              </TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </Stack>
    </>
  );
}
