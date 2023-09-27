import React, { useState } from "react";

function HomePage() {
  const [loading, setLoading] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");

  const handleSearch = () => {
    console.log(searchQuery);
    setSearchQuery("");
  };

  return (
    <div className="LandingPage">
      <h1>Home Page</h1>

      <div className="relative text-gray-600">
        <input
          type="text"
          className="border-2 border-gray-300 bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none"
          placeholder="Search..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        <button
          type="submit"
          class={`btn btn-primary ${loading === true ? "loading" : " "}`}
          onClick={handleSearch}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-4 w-4 text-gray-600"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M21 21l-4.35-4.35"
            />
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M15 11a4 4 0 11-8 0 4 4 0 018 0z"
            />
          </svg>
        </button>
      </div>
    </div>
  );
}

export default HomePage;
