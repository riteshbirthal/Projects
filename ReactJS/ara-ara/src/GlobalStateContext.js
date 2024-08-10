import React, { createContext, useReducer, useEffect } from 'react';

// Initial state
const initialState = {
  status: '',
  fanOn: false,
  lightOn: false,
  loading: false,
};

// Reducer function to handle state updates
const reducer = (state, action) => {
  switch (action.type) {
    case 'SET_STATUS':
      return { ...state, status: action.payload };
    case 'SET_FAN_ON':
      return { ...state, fanOn: action.payload };
    case 'SET_LIGHT_ON':
      return { ...state, lightOn: action.payload };
    case 'SET_LOADING':
      return { ...state, loading: action.payload };
    default:
      return state;
  }
};

// Create context
export const GlobalStateContext = createContext();

// Create provider component
export const GlobalStateProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  useEffect(() => {
    // Fetch initial state from the server or other persistent storage if needed
  }, []);

  return (
    <GlobalStateContext.Provider value={{ state, dispatch }}>
      {children}
    </GlobalStateContext.Provider>
  );
};
