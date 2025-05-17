<template>
    <div class="table_component" role="region" tabindex="0">
        <table>
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Age</th>
                    <th>E-mail</th>
                    <th>Phone Number</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="patient in patients" :key="patient.id">
                    <td>{{ patient.firstName }}</td>
                    <td>{{ patient.lastName }}</td>
                    <td>{{ patient.age }}</td>
                    <td>{{ patient.email }}</td>
                    <td>{{ patient.phone }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
    .table_component {
        overflow: auto;
        width: 100%;
    }

    .table_component table {
        border: 1px solid #dededf;
        height: 100%;
        width: 100%;
        table-layout: fixed;
        border-collapse: collapse;
        border-spacing: 1px;
        text-align: left;
    }

    .table_component caption {
        caption-side: top;
        text-align: left;
    }

    .table_component th {
        border: 1px solid #dededf;
        background-color: #eceff1;
        color: #000000;
        padding: 5px;
    }

    .table_component td {
        border: 1px solid #dededf;
        background-color: #ffffff;
        color: #000000;
        padding: 5px;
    }
</style>

<script setup>
import { ref, onMounted } from 'vue';
import { getPatients } from '../services/api.js';

const patients = ref([]);

onMounted(async () => {
    patients.value = await getPatients();
});
</script>
