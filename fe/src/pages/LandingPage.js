import React, { useState, useEffect } from 'react';
import main from '../main.svg';

function LandingPage() {
    const SPOTIFY_CLIENT_ID = process.env.REACT_APP_SPOTIFY_CLIENT_ID;
    const REDIRECT_URI = process.env.REACT_APP_REDIRECT_URI;
    const scope = 'user-read-private user-read-email playlist-modify-public playlist-modify-private user-modify-playback-state user-top-read';
    const [searchQuery, setSearchQuery] = useState('');
    const [result, setResult] = useState('');
    const [loading, setLoading] = useState(false);
    const [queryLoading, setQueryLoading] = useState(false);
    const [queries, setQueries] = useState([]);
    const authenticated = getCookieByName('accessToken') !== null;

    function getCookieByName(cookieName) {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(cookieName + '=')) {
                return cookie.substring(cookieName.length + 1);
            }
        }
        return null;
    }

    function deleteCookie(cookieName) {
        document.cookie = `${cookieName}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
    }

    const handleClearQueries = () => {
        setQueries([]);
    };

    const handleSearch = async () => {
        setQueryLoading(true);
        const data = {
            access_token: getCookieByName('accessToken'),
            token_type: 'Bearer',
            search_query: searchQuery,
        };
        setSearchQuery('');
        setResult('');

        const queryResponse = await fetch(`http://localhost:5000/query`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const queryResponseJSON = await queryResponse.json();
        console.log(queryResponseJSON);
        if (queryResponse.status === 200) {
            setQueries([...queries, searchQuery]);
            setResult(result);
        } else {
            setResult("I'm sorry, I couldn't process your request. Please input an appropriate request.");
        }
        setQueryLoading(false);
    };

    const handlePastSearch = async (query) => {
        setQueryLoading(true);
        const data = {
            access_token: getCookieByName('accessToken'),
            token_type: 'Bearer',
            search_query: query,
        };
        setSearchQuery('');
        setResult('');

        const queryResponse = await fetch(`http://localhost:5000/query`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const queryResponseJSON = await queryResponse.json();
        console.log(queryResponseJSON);
        if (queryResponse.status === 200) {
            setQueries([...queries, query]);
            setResult(result);
        } else {
            setResult("I'm sorry, I couldn't process your request. Please input an appropriate request.");
        }
        setQueryLoading(false);
    };

    const ResultComponent = ({ result }) => {
        return (
            <>
                {result.slice(0, 8) === "Couldn't" ? (
                    <div className='my-4 p-4 text-black h-72'>
                        <div role='alert' className='my-4 alert alert-error'>
                            <svg xmlns='http://www.w3.org/2000/svg' className='stroke-current shrink-0 h-6 w-6' fill='none' viewBox='0 0 24 24'>
                                <path strokeLinecap='round' strokeLinejoin='round' strokeWidth='2' d='M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z' />
                            </svg>
                            <span>{result.substring(0, result.indexOf('.'))}</span>
                        </div>
                    </div>
                ) : result.slice(0, 18) === 'To access playlist' ? (
                    <div className='my-4 p-4 text-black h-72'>
                        <div className='my-4 alert alert-success'>
                            <svg xmlns='http://www.w3.org/2000/svg' className='stroke-current shrink-0 h-6 w-6' fill='none' viewBox='0 0 24 24'>
                                <path strokeLinecap='round' strokeLinejoin='round' strokeWidth='2' d='M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z' />
                            </svg>
                            <span>
                                <a href={result.substring(result.indexOf('https'))} target='_blank' rel='noopener noreferrer'>
                                    Playlist created. Click here to be redirected.
                                </a>
                            </span>
                        </div>
                    </div>
                ) : result.length > 120 ? (
                    <div className='my-4 p-4 border rounded-lg shadow-md text-black h-72 overflow-y-auto'>
                        <h2 className='text-2xl font-bold mb-4'>Song Lyrics</h2>
                        <div>
                            <pre>{result}</pre>
                        </div>
                    </div>
                ) : result.length === 0 ? (
                    <div className='my-4 p-4 text-black h-72'>
                        <div>
                            <pre>{result}</pre>
                        </div>
                    </div>
                ) : result.slice(0, 9) === "I'm sorry" ? (
                    <div className='my-4 p-4 text-black h-72'>
                        <div role='alert' className='my-4 alert alert-error'>
                            <svg xmlns='http://www.w3.org/2000/svg' className='stroke-current shrink-0 h-6 w-6' fill='none' viewBox='0 0 24 24'>
                                <path strokeLinecap='round' strokeLinejoin='round' strokeWidth='2' d='M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z' />
                            </svg>
                            <span>
                                <p>Couldn't process your request. Please input an appropriate request.</p>
                            </span>
                        </div>
                    </div>
                ) : (
                    <div className='my-4 p-4 text-black h-72'>
                        <div className='alert alert-success'>
                            <svg xmlns='http://www.w3.org/2000/svg' className='stroke-current shrink-0 h-6 w-6' fill='none' viewBox='0 0 24 24'>
                                <path strokeLinecap='round' strokeLinejoin='round' strokeWidth='2' d='M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z' />
                            </svg>
                            <span>{result}</span>
                        </div>
                    </div>
                )}
            </>
        );
    };

    const getTokenValues = (hash) => {
        const stringAfterHashtag = hash.substring(1);
        const paramsInUrl = stringAfterHashtag.split('&');
        const tokenValues = paramsInUrl.reduce((mapping, mappingString) => {
            const [key, value] = mappingString.split('=');
            mapping[key] = value;
            return mapping;
        }, {});

        return tokenValues;
    };

    useEffect(() => {
        if (window.location.hash) {
            const { access_token, expires_in } = getTokenValues(window.location.hash);
            const expirationDate = new Date(Date.now() + expires_in * 1000).toUTCString();
            const setCookie = () => {
                document.cookie = `accessToken=${access_token}; expires=${expirationDate}; path=/`;
            };
            setCookie();
            const setUserId = async () => {
                const queryResponse = await fetch(`https://api.spotify.com/v1/me`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `Bearer ${access_token}`,
                    },
                });
                const queryResponseJSON = await queryResponse.json();
                document.cookie = `userId=${queryResponseJSON.id}; expires=${expirationDate}; path=/`;
                window.location = 'http://localhost:3000/';
            };
            setUserId();
        }
    });

    const handleLogin = () => {
        setLoading(true);
        window.location = `https://accounts.spotify.com/authorize?client_id=${SPOTIFY_CLIENT_ID}&redirect_uri=${REDIRECT_URI}&scope=${scope}&response_type=token&show_dialog=true`;
    };

    const handleLogout = () => {
        deleteCookie('accessToken');
        deleteCookie('userId');
        window.location.reload();
    };

    return (
        <div className='min-h-screen min-w-screen bg-white flex flex-col justify-center items-center'>
            {!authenticated && (
                <div className='flex flex-col items-center'>
                    <img src={main} className='w-80 h-80 mt-4 border border-gray rounded p-10 m-5' alt='Main Logo' />

                    <h1 className='text-4xl font-bold text-center text-gray-900 mb-3'>Naturify</h1>
                    <p className='text-xs text-center mb-2'>Click the button below to login with Spotify</p>
                    <button className={`btn btn-primary ${loading === true ? 'loading' : ''}`} onClick={handleLogin}>
                        Login
                    </button>
                </div>
            )}
            {authenticated && (
                <>
                    <div className='w-full h-full flex flex-col items-center'>
                        <h1 className='absolute top-10 text-4xl font-bold text-center text-gray-900'>Naturify</h1>
                        <ResultComponent result={result} />
                        <div>
                            <div className='relative text-gray-600 flex justify-center items-center mb-5'>
                                <input
                                    type='text'
                                    className='border-2 border-gray-300 bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none'
                                    placeholder='Type your query here...'
                                    value={searchQuery}
                                    onChange={(e) => setSearchQuery(e.target.value)}
                                />
                                <button type='submit' className={`btn btn-primary ml-2 ${queryLoading === true ? 'loading' : ''}`} onClick={handleSearch}>
                                    <svg xmlns='http://www.w3.org/2000/svg' className='h-4 w-4 text-black-600' fill='none' viewBox='0 0 24 24' stroke='currentColor'>
                                        <path strokeLinecap='round' strokeLinejoin='round' strokeWidth='2' d='M21 21l-4.35-4.35' />
                                        <path strokeLinecap='round' strokeLinejoin='round' strokeWidth='2' d='M15 11a4 4 0 11-8 0 4 4 0 018 0z' />
                                    </svg>
                                </button>
                            </div>

                            <div>
                                {queries.length > 0 && (
                                    <div className='flex flex-row items-center justify-center mt-4'>
                                        <h1 className='text-xl font-bold text-center text-gray-900 m-2'>Past Queries</h1>
                                        <button className='btn btn-xs btn-error' onClick={handleClearQueries}>
                                            Clear Queries
                                        </button>
                                    </div>
                                )}
                                <ul className='text-center flex flex-col'>
                                    {queries.map((query, index) => (
                                        <div className='flex flex-row'>
                                            <li className='btn btn-xs btn-neutral mb-1' onClick={() => handlePastSearch(query)} key={index}>
                                                {query}
                                            </li>
                                            <button className='btn btn-xs mx-1'>Correct</button>
                                            <button className='btn btn-xs'>Wrong</button>
                                        </div>
                                    ))}
                                </ul>
                            </div>
                        </div>

                        <button className={`fixed btn btn-primary mt-4 bottom-5 right-5 ${loading === true ? 'loading' : ''}`} onClick={handleLogout}>
                            Logout
                        </button>
                    </div>
                </>
            )}
        </div>
    );
}

export default LandingPage;
