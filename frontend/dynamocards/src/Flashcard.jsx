// import React from 'react';
import PropTypes from 'prop-types'; // Import PropTypes

function Flashcard({ term, definition, onDiscard }) {
    return (
        <div className='flashcard' style={{
            border: '1px solid #ccc',
            borderRadius: '8px',
            padding: '20px',
            margin: '10px',
            boxShadow: '0 2px 5px rgba(0,0,0,0.1)'
        }}>
            <h1>{term}</h1>
            <p>{definition}</p>
            <button onClick={onDiscard} style={{ marginTop: '10px' }}>
                Discard
            </button>
        </div>
    );
}
Flashcard.propTypes = {
    term: PropTypes.string.isRequired, // Term should be a string and is required
    definition: PropTypes.string.isRequired, // Definition should be a string and is required
    onDiscard: PropTypes.func.isRequired // onDiscard should be a function and is required
};
export default Flashcard;
