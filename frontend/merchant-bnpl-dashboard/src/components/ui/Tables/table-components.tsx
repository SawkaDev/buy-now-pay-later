import React, { useState, useEffect } from 'react';

// material-ui
import { useTheme } from '@mui/material/styles';
import {
  Box,
  FormControl,
  Grid,
  ListItemText,
  MenuItem,
  OutlinedInput,
  Pagination,
  Select,
  SelectChangeEvent,
  Stack,
  TextField,
  Typography
} from '@mui/material';

// assets
import CaretUpOutlined from '@ant-design/icons/CaretUpOutlined';
import CaretDownOutlined from '@ant-design/icons/CaretDownOutlined';
import { TableSetters } from './ReactTable';

// ==============================|| HEADER SORT ||============================== //

interface HeaderSortProps {
  column: any;
  setters: TableSetters | null;
  sort?: boolean;
}

export const HeaderSort = ({ column, sort, setters }: HeaderSortProps) => {
  const theme = useTheme();

  useEffect(() => {
    //console.log(column.isSortedDesc);
    //console.log(column.id);
    if (setters && setters.setSort) {
      //      console.log('got them');e
      if (column.isSortedDesc === undefined) {
        setters.setSort('');
        setters.setColumnFilter('');
      } else {
        setters.setSort(column.isSortedDesc);
        setters.setColumnFilter(column.id);
      }
    }
    // if you add setters then will cause issue with sorting
  }, [column.isSortedDesc, column.id]);

  return (
    <Stack direction="row" spacing={1} alignItems="center" sx={{ display: 'inline-flex' }}>
      <Box>{column.render('Header')}</Box>
      {!column.disableSortBy && (
        <Stack sx={{ color: 'secondary.light' }} {...(sort && { ...column.getHeaderProps(column.getSortByToggleProps()) })}>
          <CaretUpOutlined
            style={{
              fontSize: '0.625rem',
              color: column.isSorted && !column.isSortedDesc ? theme.palette.text.secondary : 'inherit'
            }}
          />
          <CaretDownOutlined
            style={{
              fontSize: '0.625rem',
              marginTop: -2,
              color: column.isSortedDesc ? theme.palette.text.secondary : 'inherit'
            }}
          />
        </Stack>
      )}
    </Stack>
  );
};

// ==============================|| TABLE PAGINATION ||============================== //

interface TablePaginationProps {
  gotoPage: (value: number) => void;
  setPageSize: (value: number) => void;
  pageIndex: number;
  pageSize: number;
  rows: any[];
  setters?: TableSetters;
}

export const TablePagination = ({ gotoPage, rows, setPageSize, pageSize, pageIndex, setters }: TablePaginationProps) => {
  const [open, setOpen] = useState(false);

  const handleClose = () => {
    setOpen(false);
  };

  const handleOpen = () => {
    setOpen(true);
  };

  const handleChangePagination = (event: React.ChangeEvent<unknown>, value: number) => {
    if (!setters?.setPageNumber) {
      gotoPage(value - 1);
    } else {
      setters?.setPageNumber(value - 1);
    }
  };

  const handleChange = (event: SelectChangeEvent<number>) => {
    setPageSize(+event.target.value);
  };

  var calculatedTotalRows = setters?.totalNumberOfLogs ? setters.totalNumberOfLogs : rows.length;

  return (
    <Grid container alignItems="center" justifyContent="space-between" sx={{ width: 'auto' }}>
      <Grid item>
        <Stack direction="row" spacing={1} alignItems="center">
          <Stack direction="row" spacing={1} alignItems="center">
            <Typography variant="caption" color="secondary">
              Row per page
            </Typography>
            <FormControl sx={{ m: 1 }}>
              <Select
                id="demo-controlled-open-select"
                open={open}
                onClose={handleClose}
                onOpen={handleOpen}
                // @ts-ignore
                value={pageSize}
                onChange={handleChange}
                size="small"
                sx={{ '& .MuiSelect-select': { py: 0.75, px: 1.25 } }}
              >
                <MenuItem value={5}>5</MenuItem>
                <MenuItem value={10}>10</MenuItem>
                <MenuItem value={25}>25</MenuItem>
                <MenuItem value={50}>50</MenuItem>
                <MenuItem value={100}>100</MenuItem>
              </Select>
            </FormControl>
          </Stack>
          <Typography variant="caption" color="secondary">
            Go to
          </Typography>
          <TextField
            size="small"
            type="number"
            // @ts-ignore
            value={pageIndex + 1}
            onChange={(e) => {
              const page = e.target.value ? Number(e.target.value) : 0;
              gotoPage(page - 1);
            }}
            sx={{ '& .MuiOutlinedInput-input': { py: 0.75, px: 1.25, width: 36 } }}
          />
        </Stack>
      </Grid>
      <Grid item sx={{ mt: { xs: 2, sm: 0 } }}>
        <Pagination
          // @ts-ignore
          count={Math.ceil(calculatedTotalRows / pageSize)}
          // @ts-ignore
          page={pageIndex + 1}
          onChange={handleChangePagination}
          color="primary"
          variant="combined"
          showFirstButton
          showLastButton
        />
      </Grid>
    </Grid>
  );
};

// ==============================|| COLUMN SORTING - SELECT ||============================== //

export const SortingSelect = ({ sortBy, setSortBy, allColumns, sortByCustom }: any) => {
  const [sort, setSort] = useState(sortBy);

  const handleChange = (event: SelectChangeEvent<string>) => {
    const {
      target: { value }
    } = event;
    setSort(value);
    setSortBy([{ id: value, desc: false }]);
    if (sortByCustom) {
      sortByCustom(value);
    }
  };

  return (
    <FormControl sx={{ width: 200 }}>
      <Select
        id="column-hiding"
        displayEmpty
        value={sort}
        onChange={handleChange}
        input={<OutlinedInput id="select-column-hiding" placeholder="Sort by" />}
        renderValue={(selected) => {
          const selectedColumn = allColumns.filter((column: any) => column.id === selected)[0];
          if (!selected) {
            return <Typography variant="subtitle1">Sort By</Typography>;
          }

          return (
            <Typography variant="subtitle2">
              Sort by ({typeof selectedColumn.Header === 'string' ? selectedColumn.Header : selectedColumn?.title})
            </Typography>
          );
        }}
        size="small"
      >
        {allColumns
          .filter((column: any) => column.canSort)
          .map((column: any) => (
            <MenuItem key={column.id} value={column.id}>
              <ListItemText primary={typeof column.Header === 'string' ? column.Header : column?.title} />
            </MenuItem>
          ))}
      </Select>
    </FormControl>
  );
};
