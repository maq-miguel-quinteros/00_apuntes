// para ejecutar en la terminal ingresamos node fetch

// LLAMAMOS A LAS LIBRERÍAS 
import { createStore, applyMiddleware } from 'redux'
import * as thunk from 'redux-thunk';
import axios from 'axios'


// STATE
const initialState = {
	loading: false,
	users: [],
	error: ''
}

// ACTIONS
const FETCH_USERS_REQUEST = 'FETCH_USERS_REQUEST'
const FETCH_USERS_SUCCESS = 'FETCH_USERS_SUCCESS'
const FETCH_USERS_FAILURE = 'FETCH_USERS_FAILURE'
// ACTION CREATOR
const fetchUsersRequest = () =>{
	return {
		type: FETCH_USERS_REQUEST
	}
}
const fetchUsersSuccess = users =>{
	return {
		type: FETCH_USERS_SUCCESS,
		payload: users
	}
}
const fetchUsersFailure = error =>{
	return {
		type: FETCH_USERS_FAILURE,
		payload: error
	}
}

// REDUCER
const reducer = (state = initialState, action) => {
	switch(action.type){
		case FETCH_USERS_REQUEST:
			return {
				...state,
				loading: true
			}
		break
		case FETCH_USERS_SUCCESS:
			return {
				loading: false,
				users: action.payload,
				error: ''
			}
		break
		case FETCH_USERS_FAILURE:
			return {
				loading: false,
				users: [],
				error: action.payload
			}
		break
		default:
			return state
		break
	}
}

// FUNCTION ACTION CREATOR
const fetchUsers = () => {
	return function (dispatch) {
		dispatch(fetchUsersRequest)
		axios.
		get('https://jsonplaceholder.typicode.com/users')
			.then(response => {
				const users = response.data.map(user => user.id)
				dispatch(fetchUsersSuccess(users))
			})
			.catch(error => {				
				dispatch(fetchUsersFailure(error.message))
			})
	}
}

// STORE
const store = createStore(reducer, applyMiddleware(thunk.default))
store.subscribe(() => { console.log(store.getState()) })
store.dispatch(fetchUsers())