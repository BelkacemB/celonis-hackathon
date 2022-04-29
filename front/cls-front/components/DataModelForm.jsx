import React , {useState, useEffect} from 'react';

import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';

export const DataModelForm = () => {

    const [dataModel, setDataModel] = useState(0);

    const handleChange = (event) => {
        setDataModel(event.target.value);
    };

  return (
    <div>
    <Box sx={{ minWidth: 120 }}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Dataset</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={dataModel}
          label="Age"
          onChange={handleChange}
        >
          <MenuItem value={1}>MobIS</MenuItem>
          <MenuItem value={2}>BPI 2017</MenuItem>
          <MenuItem value={3}>SAP P2P</MenuItem>
        </Select>
      </FormControl>
    </Box>
    </div>
  )
}
