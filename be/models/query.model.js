const mongoose = require('mongoose');
const QUERY_STATES = ['UNSUCCESSFUL', 'SUCCESSFUL', 'WRONG', 'CORRECT'];

const query_schema = new mongoose.Schema(
    {
        customer_id: {
            type: mongoose.Schema.Types.ObjectId,
            default: function () {
                return new mongoose.Types.ObjectId();
            },
            unique: true,
            required: true,
        },
        query: {
            type: String,
            required: true,
        },
        func: {
            type: String,
            required: true,
        },
        status: {
            type: String,
            required: true,
            enum: QUERY_STATES,
        },
    },
    {
        timestamps: true,
    }
);

const Query = mongoose.model('Query', query_schema);

module.exports = { Query };
